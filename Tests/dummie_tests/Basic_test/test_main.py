import webbrowser
import pytest
import os

from gui_maker import  listbox_gui


if __name__ == '__main__':
    
    # #First step: select the tests to execute
    listbox_items = listbox_gui()
    result =""
    py_file_name = "test_basic.py"
    
    if listbox_items == []:
        print("No selected tests")
    else:
        for i in listbox_items:
        #    result = result+ "::"+i
            result +=i+ " or "
        
        
        print("Old result : ", result)
        new_result = result.split() # cut off the last word from the string
        print("The result is: ", " ".join(new_result[:-1]))
        os.chdir('C:\Workspace\Open_canoe\Internship_work\Tests\dummie_tests\Basic_test')
        # os.system("pytest "+py_file_name+result)
        # os.system("pytest -k "+'"'+result+'"')
        os.system("pytest -k "+'"'+ " ".join(new_result[:-1])+'"')
        
    #opening the pytest html raport in browser after executing the tests
    webbrowser.open_new_tab("C:\Workspace\Open_canoe\Internship_work\Tests\dummie_tests\Basic_test\pytest_html_report.html")
        
   
    

    
    