import sys

# As initialized upon program startup, the first item of this list, path[0], is the directory containing the script that was used to invoke the Python interpreter.
# If you want a particular directory to come first, simply insert it at the head of sys.path
sys.path.insert(1, "Automation_Framework\Canoecontrol")
sys.path.insert(1, "Automation_Framework\Tenmacontrol")

from open_canoeobj import Canoe
from tenma_control import Tenm

#obj is an instance of Canoe class
#tenma_obj is an instance of Tenm class
obj = Canoe() # make it global
tenma_obj = Tenm()

def Calibration_datase():
    for i in range(0, 3): # after 3 unsuccessful tries, the program will automatically goes on until i find out what has to be done
        obj.Connect_DOIP()
        obj.TesterPresent() 
        # if rbeol == False -> diop connect
        if obj.RBEOL() == False:
            print("RBEOL not working")
        else:
            print("RBEOL working")
            if obj.RBEOL_unlock() == False:
                print("RBEOL unlock not working")
            else:  
                print("RBEOL unlock working")    
            # if service not supported:
            #   resolve with flag
                # RBOEL 
                # RBOEL_unlock
                break
        # in fct de returnul de la rbol caz 2 -> restart simulare , back to doip connect si cazul 2 se comporta ca si cand avem un false la return
        # daca e 1 pass or continue
    obj.RBEOL_unlock()
    # if service not supported:
    #   resolve with flag
        # RBOEL 
        # RBOEL_unlock
    for i in range(0, 2): # 2 tries only
        if obj.send_diagnostic("MPC03T", '2EF1ABFF') != "6EF1AB" :
        # se verifica daca 6EF1AB -> positive response and pass
        # not positive response send again diag 2EF1ABFF
            obj.send_diagnostic("MPC03T", '2EF1ABFF')
        else:
            break
    obj.send_diagnostic()# se trimite hexstringul
    tenma_obj.restart_tenma() # this implicitly is restarting the camera
    obj.restart_canoe() # restart simulation
    obj.Read_DTC() 
    
    
def GVC_parametrization():
    obj.Connect_DOIP()
    obj.TesterPresent()
    obj.ExtendedDiag()  #diag session button
    obj.send_diagnostic("MPC03T", '22F100') 
    obj.send_diagnostic("MPC03T", '2E100500') 
    obj.send_diag_hex_string()# not implemented yet
    # need to be implemented a function for hexstring
    tenma_obj.restart_tenma() # this implicitly is restarting the camera
    obj.restart_canoe() # restart simulation
    obj.Read_DTC()
    
def manula_initial_calibration():
    obj.Connect_DOIP()
    obj.TesterPresent() 
    obj.RBEOL()
    obj.RBEOL_unlock()
    obj.send_diagnostic("MPC03T", 'special string') #REPLACE diag_ecu_qualifier_name and "special string" with valid names
    obj.restart_canoe() # restart simulation
    obj.Read_DTC()
    
def updating_camera_position():
    obj.Connect_DOIP()
    obj.TesterPresent()
    obj.ExtendedDiag() #diag session button
    obj.send_diagnostic("MPC03T", '22F100') #REPLACE diag_ecu_qualifier_name with valid name
    obj.send_diag_hex_string()# not implemented yet
    obj.ReadData("221200")#not implemented yet
    tenma_obj.restart_tenma() # this implicitly is restarting the camera
    obj.restart_canoe() # restart simulation
    obj.Read_DTC()
    
#calling the functions
Calibration_datase()
GVC_parametrization()
manula_initial_calibration()
updating_camera_position()