
import PySimpleGUI as sg
import pytest
import ast

# functions section
def gui_interface(test_name):
    
    layout = [
        [sg.Text(test_name)],
        [sg.Button('Passed'), sg.Button('Failed'), sg.Button('Skipped')],
        [sg.Text('Skipped message'), sg.Combo( ['Test not useful',
                                               'Old test',
                                               'Test cannot be used now',
                                               'Test not finished'], key = 'Combo', enable_events=True, visible = False)],
        [sg.Text('Failed message'), sg.Input(enable_events=True, key = '-Fail-', visible = False)],
        [sg.Button('Done', key = 'Done_for_Failed', visible=False)],
        [sg.Button('Done', key = 'Done_for_Skipped', visible=False)],
    ]
    
    window = sg.Window('Basic tests', layout)
   
    result = []
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED :
            break
        
        elif event == 'Passed':
            result.append("passed")
            break
            
        elif event == 'Failed':
            window["-Fail-"].update(visible = True)
            window['Failed'].update(disabled= True)
            window["Combo"].update(visible = False)
            window['Skipped'].update(disabled = False)
            window['Done_for_Skipped'].update(visible = False)
            
        elif event =='-Fail-':
            window["Done_for_Failed"].update(visible = True)
            
        elif event == 'Done_for_Failed':
            # print(values['-Fail-'])
            # break
            result.append("failed")
            result.append(values['-Fail-'])
            break
            
        elif event == "Skipped":
            window["Combo"].update(visible = True)
            window['Skipped'].update(disabled= True)
            window["-Fail-"].update(visible = False)
            window['Failed'].update(disabled = False)
            window['Done_for_Failed'].update(visible = False)
            
        elif event =='Combo':
            window["Done_for_Skipped"].update(visible = True)
            # print(values['Combo'])
            
        elif event == 'Done_for_Skipped':
            # pytest.skip(values['Combo'])
            result.append("skipped")
            result.append(values['Combo'])
            break
           
    window.close()
    return result

def interpret_result(res):
    if res[0] == "passed":
        assert True
    elif res[0] == "failed":
        assert False, res[1]
    elif res[0] == "skipped":
        assert pytest.skip(str(res[1]))
    


# this functon is realized with the help of abstract syntax trees (ast) to extract the function names
def get_test_names(test_file):
    function_names = []
    o = open(test_file, "r")
    text = o.read()
    p = ast.parse(text)
    for node in ast.walk(p):
        if isinstance(node, ast.FunctionDef):
            function_names.append(node.name)
            
    return function_names


# test_function_names = get_test_names("C:\Workspace\Open_canoe\Internship_work\Tests\dummie_tests\Basic_test/test_basic.py")
# print(test_function_names)

def listbox_gui():
    
    test_names = get_test_names("C:\Workspace\Open_canoe\Internship_work\Tests\dummie_tests\Basic_test/test_basic.py")
    
    
    layout = [
        [sg.Text("Select test/s to be executed")],
        [sg.Checkbox("Run all tests", enable_events=True, key = 'Check'), sg.Checkbox("Clear listbox", enable_events=True, key = 'uncheck')],
        [sg.Listbox(values=test_names, select_mode= sg.LISTBOX_SELECT_MODE_MULTIPLE, expand_y=False, enable_events= True, key= 'LIST', size=(30, 20))],
        [sg.Button("Execute")]
        
    ]
    
    window = sg.Window('Basic tests', layout, size = (300, 450))
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED :
            break
        elif event == 'Check':
            num_list_items = len(test_names) # used the list of test names instead of listbox values / only way it worked
            window['LIST'].update(set_to_index = list(range(num_list_items))) # set to item get a list => multiple element from listbox will be selected
            #set_to _index receives one parameter => only one list item will be selected  
            window['uncheck'].update(False)
        elif event == 'uncheck':
            window['LIST'].update(set_to_index = [])
            window['Check'].update(False)
        elif event =="Execute":
            result =  values['LIST'] # not necessary a break after return to close the gui
            break
       
    window.close()
    return result 

# print("Running tests: ", listbox_gui())





