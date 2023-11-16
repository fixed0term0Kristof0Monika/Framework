"""Execute XML Test Cases without a pass verdict"""
from time import sleep
import win32com.client as win32
import configparser
import time
from pandas.core.computation.expressions import set_test_mode
import pythoncom

# C:Users/Public\Documents/Vector/CANoe\Sample Configurations 16.2.55/CAN\Diagnostics/UDSBasic/UDSBasic.cfg
testComplete = False

class TestModuleEvents(object):
    def OnReportGenerated(self,Success, SourceFullName, GeneratedFullName):
        global testComplete
        print("Report Generated")
        testComplete = True
        
    def OnStop(self, value):
        global testComplete
        print("Test Module Stopped")
        testComplete = True

    def OnStart(self):
        global testComplete
        print("Test Module Started")
        testComplete = True

class TestConfigurationEvents(object):
    def OnStart(self):
        global testComplete
        print("Measurement Started")
        testComplete = False
        
    def OnStop(self):
        global testComplete
        print("Measurement Stopped")
        testComplete = True

config = configparser.RawConfigParser()
config.read('usecase02_configuration.properties')
configurationPath = config.get('TESTCONFIGURATION', 'configurationpath')
testspec = config.get('TESTCONFIGURATION', 'testspecification')

CANoe = win32.DispatchEx("CANoe.Application")
CANoe.Open(configurationPath)

testSetup = CANoe.Configuration.TestSetup
testSetup.TestEnvironments.Add(testspec)
test_env = testSetup.TestEnvironments.Item('Test Environment')
test_env = win32.CastTo(test_env, "ITestEnvironment2")


# print(report.FullName)

# Get the XML TestModule (type <TSTestModule>) in the test setup
test_module = test_env.TestModules.Item('Tester')
CANoe.Measurement.Start()
sleep(5)   # Sleep because measurement start is not instantaneous

win32.WithEvents(test_module, TestModuleEvents)
test_module.Start()

# sleep(60)

while not testComplete:
    time.sleep(1)

# test_module.Stop()
print(test_module.Verdict)