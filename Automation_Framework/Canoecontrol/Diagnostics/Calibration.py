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
    
    obj.Connect_DOIP()
    obj.TesterPresent() 
    obj.RBEOL()
    # if rbeol == False -> diop connect
    # in fct de returnul de la rbol caz 2 -> restart simulare , back to doip connect 
    # daca e 1 pass
    obj.RBEOL_unlock()
     # if service not supported:
    #   resolve with flag
        # RBOEL 
        # RBOEL_unlock
    obj.send_diagnostic("diag_ecu_qualifier_name", '2EF1ABFF') #REPLACE diag_ecu_qualifier_name with valid name
    # se verifica daca 6EF1AB -> positive response and pass
    # not positive response send again diag 2EF1ABFF
    obj.send_diagnostic()# se trimite hexstringul
    tenma_obj.restart_tenma() # this implicitly is restarting the camera
    obj.restart_canoe() # restart simulation
    obj.Read_DTC() 
    
def GVC_parametrization():
    obj.Connect_DOIP()
    obj.TesterPresent()
    obj.ExtendedDiag()  #diag session button
    obj.send_diagnostic("MPC03T", '22F100') #REPLACE diag_ecu_qualifier_name with valid name
    obj.send_diagnostic("diag_ecu_qualifier_name", '2E100500') #REPLACE diag_ecu_qualifier_name with valid name
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
    obj.send_diagnostic("diag_ecu_qualifier_name", 'special string') #REPLACE diag_ecu_qualifier_name and "special string" with valid names
    obj.restart_canoe() # restart simulation
    obj.Read_DTC()
    
def updating_camera_position():
    obj.Connect_DOIP()
    obj.TesterPresent()
    obj.ExtendedDiag() #diag session button
    obj.send_diagnostic("diag_ecu_qualifier_name", '22F100') #REPLACE diag_ecu_qualifier_name with valid name
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