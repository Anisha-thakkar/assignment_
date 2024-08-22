# passwd = input("Enter password: ")
# a=0
# b=0
# c=0
# if len(passwd)>=8:
#     a = 1
# for i in passwd:
#     if i.isdigit():
#         b=1
#     if i.isupper():
#         c=1
# if a==1 and b==1 and c==1:
#     print("True")
# else:
#     print("False")

passwd = input("Enter password: ")

results={"length":False,"digit":False,"Uppercase":False}

if len(passwd)>=8:
    results["length"]=True

for i in passwd:
    if i.isdigit():
        results["digit"]=True
    if i.isupper():
        results["Uppercase"]=True

if all(results.values()):
    print("Strong Password")
else:
    print("Weak Password")

