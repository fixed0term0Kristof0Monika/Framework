# https://realpython.com/pytest-python-testing/
# https://www.testim.io/blog/using-pytest-fixtures/
# https://github.com/prashanth-sams/pytest-html-reporter/blob/master/README.rst

# from tenma_control import Tenm

# powersupply = Tenm()

def test_if_reset_correctly_voltage():
    # set_Vvalue = powersupply.setV()
    # get_Vvalue = powersupply.getV()
    set_Vvalue = 20.3
    get_Vvalue = 20.3
    assert set_Vvalue == get_Vvalue
    
    
def test_if_reset_correctly_current():
    # set_Cvalue = powersupply.setV()
    # get_Cvalue = powersupply.getV()
    set_Cvalue = 2.5
    get_Cvalue = 2.7
    assert set_Cvalue == get_Cvalue 