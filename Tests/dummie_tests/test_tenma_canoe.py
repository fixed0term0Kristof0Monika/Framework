import sys, os
from time import sleep as wait
import pytest

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from tenmacontrol.tenma_control import Tenm
from Canoecontrol.open_canoeobj import Canoe

#object declaration
tenma_obj = Tenm()
canoe_obj = Canoe()

def test_Script12(canoeOpenClose, tenmaOnOff):
    #preparation
    tenma_obj.tenma_off()
    wait(1)
    #stimulation
    wait(1)
    
    #check simulation
    # check if the message is sent from the RCU
    if canoe_obj.get_signal("RCU_System_Status", "System_Status_MsgCnt") >=0 and canoe_obj.get_signal("MRR_Sensor_Information", "Sensor_Information_MsgCnt") >=0 and canoe_obj.get_signal("MPC_System_Status", "MPC_System_Status_MsgCnt") >= 0:
        assert True
    else:
        assert False
        
  
# RCU System Status after 2 seconds
def test_Script34(canoeOpenClose, tenmaOnOff):
    #stimulation
    wait(2) 
    #Check result:
    assert canoe_obj.get_signal("RCU_System_Status", "System_Status") == 0
        
        
# warning level
def test_Script52(canoeOpenClose, tenmaOnOff):
    results= []
    # action
    for i in range(1, 5):
        canoe_obj.set_signal("MRR_Warning_Message", "Warning_Message_CRC", i)
        wait(3)
        results.append(canoe_obj.get_signal("RCU_System_Status", "System_Status"))
    print(results)
    #check results
    if results == [0.0, 0.0, 0.0, 0.0]:
         assert True
    else:
        assert False
        
    
def test_Script48(canoeOpenClose, tenmaOnOff):
    #stimulation
    wait(2) 
    #Check result: 
    assert canoe_obj.get_signal("RCU_Vehicle_Velocity", "Vehicle_Velocity_CRC") >=  80
   
def test_Script13_1(canoeOpenClose, tenmaOnOff):
    #stimulation
    tenma_obj.setV(24)
    #check results
    assert canoe_obj.send_diagnostic() 
    
def test_Script13_2(canoeOpenClose, tenmaOnOff):
    #stimulation
    tenma_obj.setV(8)
    #check results
    assert canoe_obj.send_diagnostic() 
    
    
@pytest.fixture(scope = "module")
def canoeOpenClose():
    
    canoe_obj.open_Canoe() 
    wait(5)
    canoe_obj.str_measur()  
    
    yield canoe_obj
    wait(2)
    canoe_obj.stop_measur()    
    canoe_obj.close_Canoe()  


# same fixture with tenma
@pytest.fixture
def tenmaOnOff():
  #stimulation
    tenma_obj.tenma_off()
    wait(2)
    tenma_obj.tenma_on()
    tenma_obj.setV(12)
    yield tenma_obj
    wait(1)
    tenma_obj.tenma_off()
