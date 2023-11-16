import json
import glob


# with open("C:\Workspace\Open_canoe/tenmacontrol\output.json", "r") as json_file:
#         data = json.load(json_file)
#         for j in data['content']['suites']:
#                 j_str= str(j)
#                 for i in data['content']['suites'][j_str]['tests']:
#                         i_str= str(i)
#                         print(data['content']['suites'][j_str]['tests'][i_str]['test_name'])
#                         print(data['content']['suites'][j_str]['tests'][i_str]['status'])
#                         print(data['content']['suites'][j_str]['tests'][i_str]['message'])
        
f = glob.glob("C:\Workspace\Open_canoe/tenmacontrol/archive/*.json")
for i, val in enumerate(f):
        # print(i)
        with open(val) as json_file:
                data = json.load(json_file)
                for j in data['content']['suites']:
                        j_str= str(j)
                        for i in data['content']['suites'][j_str]['tests']:
                                i_str= str(i)
                                print(data['content']['suites'][j_str]['suite_name'])
                                print(data['content']['suites'][j_str]['tests'][i_str]['test_name'])
                                print(data['content']['suites'][j_str]['tests'][i_str]['status'])
                                print(data['content']['suites'][j_str]['tests'][i_str]['message'])
                               
                        
                        
       
                
                
                
                
                
                
                
                
                
#                 table= '''
#                         <!DOCTYPE html>
#                         <html lang="en">
#                         <head>
#                                 <meta charset="UTF-8">
#                                 <meta name="viewport" content="width=device-width, initial-scale=1.0">
#                                 <title>Document</title>
#                         </head>
#                         <body>
                        
#                                 <table style="width:100%; margin:2% auto;">
#                                                 <thead style = "border-bottom: solid black;">
#                                                         <tr>
#                                                                 <th>Suite</th>
#                                                                 <th>Test Case</th>
#                                                                 <th>Status</th>
#                                                                 <th>Time (s)</th>
#                                                                 <th>Error Message</th>
#                                                         </tr>
#                                                 </thead>
#                                                 <tbody>
#                                                         __test_archive_row__
#                                                 </tbody>
#                                 </table>
                        
#                         </body>
#                         </html>
#                 '''
#                 append_rows = '''
#                         <tr>
                        
#                         </tr>
#                 '''
                
        