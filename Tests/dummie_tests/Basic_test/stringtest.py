
# import ast

# class FuncLister(ast.NodeVisitor):

#     def visit_FunctionDef(self, node):
        
#         print('FunctionDef', node.name)
#         self.generic_visit(node)

# with open('C:\Workspace\Open_canoe\Internship_work\Tests\dummie_tests\Basic_test/test_basic.py', 'r') as f:
#     tree = ast.parse(f.read())
#     print(FuncLister().visit(tree))

from time import sleep as wait

def Connect_DOIP(): 
    i = 0   
    while i<10:
       print("i less then 10")
       i=i+1
            
        # if self.get_EnvVar("Env_DoipNetStatus") != "":
        #     break
    print("hi")

Connect_DOIP()
