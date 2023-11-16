from open_canoeobj import Canoe

#obj is an instance of Canoe class
obj = Canoe() # make it global

def Calibration_datase():
    
    obj.Connect_DOIP()
    obj.testerPresent() # not implemented yet
    obj.RBEOL()
    obj.RBEOL_unlock()
    obj.send_diagnostic("diag_ecu_qualifier_name", '2EF1ABFF') #REPLACE diag_ecu_qualifier_name with valid name
    obj.send_diag_hex_string()# not implemented yet
    obj.restart_camera() #not implemented yet
    #restart simulation:
    obj.stop_measur()
    obj.str_measur()
    
def GVC_parametrization():
    obj.Connect_DOIP()
    obj.testerPresent()
    obj.extended_diag() #not implemented yet
    obj.send_diagnostic("diag_ecu_qualifier_name", '22F100') #REPLACE diag_ecu_qualifier_name with valid name
    obj.send_diagnostic("diag_ecu_qualifier_name", '2E100500') #REPLACE diag_ecu_qualifier_name with valid name
    obj.send_diag_hex_string()# not implemented yet
    obj.restart_camera() #not implemented yet
    #restart simulation:
    obj.stop_measur()
    obj.str_measur()
    obj.Read_DTC()
    
def manula_initial_calibration():
    obj.Connect_DOIP()
    obj.testerPresent() # not implemented yet
    obj.RBEOL()
    obj.RBEOL_unlock()
    obj.send_diagnostic("diag_ecu_qualifier_name", 'special string') #REPLACE diag_ecu_qualifier_name and "special string" with valid names
    #restart simulation:
    obj.stop_measur()
    obj.str_measur()
    obj.Read_DTC()
    
def updating_camera_position():
    obj.Connect_DOIP()
    obj.testerPresent()
    obj.extended_diag() #not implemented yet
    obj.send_diagnostic("diag_ecu_qualifier_name", '22F100') #REPLACE diag_ecu_qualifier_name with valid name
    obj.send_diag_hex_string()# not implemented yet
    obj.ReadData("221200")#not implemented yet
    obj.restart_camera() #not implemented yet
    #restart simulation:
    obj.stop_measur()
    obj.str_measur()
    obj.Read_DTC()
    
#calling the functions
Calibration_datase()
GVC_parametrization()
manula_initial_calibration()
updating_camera_position()