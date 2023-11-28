
from py_canoe import CANoe
from time import sleep as wait
import tkinter.filedialog
import tkinter as tk
from win32com.client import *
from win32com.client.connect import *
import sys

# As initialized upon program startup, the first item of this list, path[0], is the directory containing the script that was used to invoke the Python interpreter.
sys.path.insert(1, "Automation_Framework\Tenmacontrol")

from tenma_control import Tenm
from functions import *
 
#implementing a class which has the following modules:
#open CANoe by user input of the specific configuration file
#start the measurements
#the set signal method
# get signal method
# stop measurements
# close CANoe
#seat test for config path

 
class Canoe:
    
    def __init__(self):
        self.canoe_inst = CANoe()
                
    # module for opening CANoe
    def open_Canoe(self):
        root = tk.Tk()
        root.withdraw()
        file_path = tkinter.filedialog.askopenfilename()
        try:
            self.canoe_inst.open(canoe_cfg=file_path)
        except:
            print("Wrong file or the file is already open")
        
    # starting measurements
    def str_measur(self):
        wait(5)
        self.canoe_inst.start_measurement()
        
    #get signal 
    def get_signal(self, message, signal, channel= "ETHERNET", can_nr = 1): #default values: channel / can_nr //ETHERNET - default
        try:
            return self.canoe_inst.get_signal_value(channel, can_nr, message, signal)
        except:
            print("not good values")
        
        
    
    #set signal
    def set_signal(self, message, signal, value, channel= "ETHERNET", can_nr = 1):  #default values: channel / can_nr
        #can_nr, value integers; messages str
        try:
            self.canoe_inst.set_signal_value(channel, can_nr, message, signal, value)
            wait(5)
        except:
           print(" not good values")
                
    def set_syst_signal(self, sys_var_name, value ):
        try:
            self.canoe_inst.set_system_variable_value(sys_var_name, value)
        except:
            if(not isinstance(sys_var_name, str) ):
                print("Wrong system variable namespace or name")
            elif(not isinstance(value, int)):
                print("Value is not a valid integer!")
            
    def get_syst_signal(self, sys_var_name):
        try:
           return self.canoe_inst.get_system_variable_value(sys_var_name)
        except:
             if(not isinstance(sys_var_name, str)):
                print("Wrong system variable namespace or name,")
    
    def send_diagnostic(self,diag_ecu_qualifier_name , request, request_in_bytes = True):
        return self.canoe_inst.send_diag_request(diag_ecu_qualifier_name, request, request_in_bytes)
    
    # Environment variables manipulation
    def get_EnvVar(self, var):
        try:
            return self.canoe_inst._CANoe__canoe_objects.get("Environment").GetVariable(var).Value
        except ValueError:
            print ("Couldn't find value")

    def set_EnvVar(self, var, value):
        # set the environment varible
        result = self.canoe_inst._CANoe__canoe_objects.get("Environment").GetVariable(var)
        result.Value = value
        wait(1)
        if( self.get_EnvVar(var) == value):
            print("Set to: ", self.get_EnvVar(var))
        else:
            raise ValueError("Value not corresponding")
            
    #Connectivity with ethernet 
    def Connect_DOIP(self):
        var = "Env_DoipConnectVeh"   
        self.set_EnvVar(var, 1)
        wait(2) 
        self.set_EnvVar(var, 0)

        i =0 # flag
        while self.get_EnvVar("Env_DoipNetStatus") != "DOIP CONNECTION ESTABILISHED":
            self.restart_canoe() # restart simulation
            if i == 1:
               Tenm.restart_tenma() #restart camera
            if i > 1:
                return False
            self.set_EnvVar(var, 1)
            wait(2) 
            self.set_EnvVar(var, 0)
            i+=1
        return True
     
            
    # Reading DTC   
    def Read_DTC(self):
        try:
            self.set_EnvVar("Env_DoipConnectVeh", 1)
            wait(2)
            self.set_EnvVar("Env_DoipConnectVeh", 0)   
        except AttributeError:
            print("Wrong value or Environment variable")    
        rec= self.get_EnvVar("Env_DoipDirectReceive")   
        # put the received Diagnostic code into a list
        listOfDiag = splitDiagResponse(rec)
        print(listOfDiag)
        
    #RBEOL
    def RBEOL(self):
        try:
            self.set_EnvVar("Env_RBEOL", 1)
            wait(2)
            self.set_EnvVar("Env_RBEOL", 0)   
        except AttributeError:
            print("Wrong value or Environment variable")
            
        rec= self.get_EnvVar("Env_DoipDirectReceive")
        if rec == "C0B501":
            return True # "Positive response" 
        else:
            self.Rastart_camera()
            # if 5101 (envdirectreceived) -> positive response 
            
            if self.get_EnvVar("Env_DoipDirectReceive") == "5101": 
                if Tenm.getC()> 1.3:
                    return True # posistive response
            # se verifica consumul de pe tenma if >1.3A -> pass
                                                # else -> restart tenma return 1
                else:                           # se reia doip connect return 2
                    Tenm.restart_tenma() 
                    return False# "Service not supported" 
            
       
        
    #RBEOL_unlock
    def RBEOL_unlock(self):
        try:
            self.set_EnvVar("Env_JLR_Prog_Unlock", 1)
            wait(2)
            self.set_EnvVar("Env_JLR_Prog_Unlock", 0)   
        except AttributeError:
            print("Wrong value or Environment variable")
        
        rec= self.get_EnvVar("Env_DoipDirectReceive")    
        if rec == "6762":
            return True #"Positive response" 
        elif rec == "7F2712":
            return False # "Service not supported" 
       
       
    def TesterPresent(self):
        # set the tester present button to on
        self.set_EnvVar("Env_DoipTesterPresentOnOff", 1)
        
    def ExtendedDiag(self): #Diag. Session button manipulation
        self.set_EnvVar("Env_DoipExtSession", 1)
        
    def Rastart_camera(self):
        # 1101 has to be introduced to the EnvDirectSend input field
        self.send_diagnostic("MPC03T", "1101") # don't know which diag_name to put
            
        
    #stop measurements
    def stop_measur(self):
        wait(5)
        self.canoe_inst.stop_measurement()
        
    #close CANoe
    def close_Canoe(self):
        wait(5)
        self.canoe_inst.quit()
        
    # function to restart the measurments 
    def restart_canoe(self):
        # wait odule is included in the stop_measur() / str_measur() functions
        self.stop_measur()
        self.str_measur()

