
from collections import OrderedDict
import openpyxl
from py_canoe import CANoe
from time import sleep as wait
import tkinter.filedialog
import tkinter as tk
from win32com.client import *
from win32com.client.connect import *
 
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
    def Connect_DOIP(self, var):    
        while self.get_EnvVar("Env_DoipNetStatus") == "":
            try:
                self.set_EnvVar(var, 1)
                wait(2)
                self.set_EnvVar(var, 0)   
            except AttributeError:
                print("Wrong value or Environment variable")
            
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
            return "Positive response"
        elif rec == "7F8011":
            return "Service not supported"
        else:
            return "Error"
        
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
            return "Positive response"
        elif rec == "7F2712":
            return "Service not supported"
        else:
            return "Error"    
     
            
        
    #stop measurements
    def stop_measur(self):
        wait(5)
        self.canoe_inst.stop_measurement()
        
    #close CANoe
    def close_Canoe(self):
        wait(5)
        self.canoe_inst.quit()
        

# additional function 
def splitDiagResponse(str_var):
    usefull_code = str_var[6:]
    firstSix = str_var[:6]
    mylist = []
    if firstSix != "59027B":
        return "Error"
    else:
        if len(str_var)==6:
            return mylist
            
        elif len(str_var)>6:
            
             mylist = []
             for i in range(0, len(usefull_code), 8):
                mylist.append(usefull_code[i:i+8])
            
             DTC_dict = {}
             DTC_list = []
             for i in  mylist:
                DTC_dict["Dtc_code"] = i[:6]
                DTC_dict["DTC_status"] = i[6:]
                DTC_dict["DTC_name"] =  find_DTCnames(i[:6])
                
                # print("dict =" , DTC_dict)
                DTC_list.append(DTC_dict.copy())
                # print("list = ", DTC_list)
                     
    return DTC_list 
     
            
def find_DTCnames(value):  
    wb = openpyxl.open("C:\Workspace\Open_canoe\Internship_work\Automation_Framework\Dem_Cust_UniqueID_Listexcell.xlsx")
    sheet = wb.active
    
    dtc_names = []
    for row in sheet.iter_rows(min_row =2, max_row = 228, min_col = 1, max_col =4, values_only = True):
        if value == row[-1][2:]:
            
            dtc_names.append(row[2])
    result = list(OrderedDict.fromkeys(dtc_names))
    return result[0]


def findEvenetParam(value):
    wb = openpyxl.open("C:\Workspace\Open_canoe\Internship_work\Automation_Framework\Dem_Cust_UniqueID_Listexcell.xlsx")
    sheet = wb.active       
    evenetparam = []
    for row in sheet.iter_rows(min_row =2, max_row = 228, min_col = 1, max_col =4, values_only = True):
        if value == row[-1][2:]: 
            evenetparam.append(row[0])  
            
    return evenetparam  

# callcaplfunc, clear window, readtext from writewindow