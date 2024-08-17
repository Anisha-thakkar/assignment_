import csv

dict_ = {1:'one',2:'two',3:'three',4:'four',5:'five'}

def get_fun(str1):
    print(str1)
def create_fun(str1,str2,d):
    d.update({int(str1):str2})
    print(d)
def update_fun(str1,str2,d):
    d[int(str1)]=str2
    print(d)
def delete_fun(str1,d):
    del d[int(str1)]
    print(d)

with open('test1.csv', 'r') as read_obj: 
    csv_reader = csv.reader(read_obj) 
    list_of_csv = list(csv_reader) 

    #print(list_of_csv[1][0]) 
    for i in range(len(list_of_csv)):
        if(list_of_csv[i][0]=='GET'):
            get_fun(list_of_csv[i][1])
        elif(list_of_csv[i][0]=='CREATE'):
            create_fun(list_of_csv[i][1],list_of_csv[i][2],dict_)
        elif(list_of_csv[i][0]=='UPDATE'):
            update_fun(list_of_csv[i][1],list_of_csv[i][2],dict_)
        else:
            delete_fun(list_of_csv[i][1],dict_)