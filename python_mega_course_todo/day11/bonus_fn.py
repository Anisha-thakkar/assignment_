def get_avg():
    with open("files/data.txt",'r') as file:
        data=file.readlines()
    values= data[1:]
    values= [float(i) for i in values]
    average= sum(values)/len(values)
    print(values)
    return average
print(get_avg())