from gui_maker import gui_interface, interpret_result

import pytest

# test section
def test_Flashing():
    result = gui_interface("1. Flashing test")
    interpret_result(result)

def test_SWversion():
    result = gui_interface("2. SW version test")
    interpret_result(result)
    
def test_HW():
    result = gui_interface("3. Check HW numbers in the DIDs")
    interpret_result(result)

def test_ManualCalibration():
    result = gui_interface("4. Test manual calibration")
    interpret_result(result)
  
def test_StaticCalibration():
    result = gui_interface("5. Static calibration test")
    interpret_result(result)

def test_VDET0():
    result = gui_interface("6. Check VDET recognition with static image and speed 0 kph")
    interpret_result(result)
    
def test_VDET30():
    result = gui_interface("7. Check VDET recognition with static image and speed > 30 kph")
    interpret_result(result)

def test_ODET0():
    result = gui_interface("8. Check ODET recognition with static image and speed 0 kph")
    interpret_result(result)
  
def test_ODET30():
    result = gui_interface("9. Check ODET recognition with static image and speed > 30 kph")
    interpret_result(result)

def test_Lane0():
    result = gui_interface("10. Check Lane recognition with static image and speed 0 kph")
    interpret_result(result)

def test_Lane30():
    result = gui_interface("11. Check Lane recognition with static image and speed > 30 kph")
    interpret_result(result)

def test_Beta0():
    result = gui_interface("12. Check switch recognition with static image and speed 0 kph - Beta Release")
    interpret_result(result)

def test_Beta30():
    result = gui_interface("13. Check switch recognition with static image and speed > 30 kph - Beta Release")
    interpret_result(result)

def test_Next0():
    result = gui_interface("14. Check Road Sign Recognition with static image and speed 0 kph - next releases")
    interpret_result(result)

def test_Next30():
    result = gui_interface("15. Check Road Sign Recognition with static image and speed > 30 kph - next releases")
    interpret_result(result)

def test_SetSpeed():
    result = gui_interface("16. Set speed signal to invalid value - check that DTC is triggered and functionality is limited")
    interpret_result(result)

def test_SetYaw():
    result = gui_interface("17. Set yaw rate signal to invalid value - check that DTC is triggered and functionality is limited")
    interpret_result(result)

def test_MPCBelow():
    result = gui_interface("18. Set MPC3 Power Supply below limit? - check DTC")
    interpret_result(result)

def test_MPCAbove():
    result = gui_interface("19. Set MPC3 Power Supply above limit? - check DTC")
    interpret_result(result)

         
