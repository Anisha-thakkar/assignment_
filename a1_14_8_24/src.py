import csv

dict_ = {1:'one',2:'two',3:'three',4:'four',5:'five'}

def get_fun(str1):
    print(str1)
def create_fun(str1,str2,d):
    d.update({str1:str2})
    print(d)

with open('test1.csv', 'r') as read_obj: 
    csv_reader = csv.reader(read_obj) 
    list_of_csv = list(csv_reader) 

    #print(list_of_csv[1][0]) 
    for i in range(len(list_of_csv)):
        if(list_of_csv[i][0]=='GET'):
            get_fun(list_of_csv[i][1])
        else:
            create_fun(list_of_csv[i][1],list_of_csv[i][2],dict_)