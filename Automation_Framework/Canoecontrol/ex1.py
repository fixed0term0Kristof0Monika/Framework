from collections import OrderedDict
import openpyxl

mystr = "59027B10F4F32345FFED2349FFED23"
# change output to dictionary

def sfs(stringds):
    remained_str = stringds[6:]
    firstSix = stringds[:6]
    mylist = []
    if firstSix != "59027B":
        return "Error"
    else:
        if len(stringds)==6:
            return mylist
            
        elif len(stringds)>6:
            mylist = []
            for i in range(0, len(remained_str), 8):
                mylist.append(remained_str[i:i+8])
            
            DTC_dict = {}
            DTC_list = []
            for i in  mylist:
                DTC_dict["Dtc_code"] = i[:6]
                DTC_dict["DTC_status"] = i[6:]
                DTC_dict["DTC_name"] =  find_DTCnames(i[:6])
        
                # print("dict =" , DTC_dict)
                DTC_list.append(DTC_dict.copy())
                # print("list = ", DTC_list)
                     
    return DTC_list


def find_DTCnames(value):  
    wb = openpyxl.open("C:\Workspace\Open_canoe\Internship_work\Automation_Framework\Dem_Cust_UniqueID_Listexcell.xlsx")
    sheet = wb.active
    
    dtc_names = []
    for row in sheet.iter_rows(min_row =2, max_row = 228, min_col = 1, max_col =4, values_only = True):
        if value == row[-1][2:]:
            
            dtc_names.append(row[2])
    result = list(OrderedDict.fromkeys(dtc_names))
    return result[0]


def findEvenetParam(value):
    wb = openpyxl.open("C:\Workspace\Open_canoe\Internship_work\Automation_Framework\Dem_Cust_UniqueID_Listexcell.xlsx")
    sheet = wb.active       
    evenetparam = []
    for row in sheet.iter_rows(min_row =2, max_row = 228, min_col = 1, max_col =4, values_only = True):
        if value == row[-1][2:]: 
            evenetparam.append(row[0])  
            
    return evenetparam  

   
print( "the initial string", sfs(mystr))  


