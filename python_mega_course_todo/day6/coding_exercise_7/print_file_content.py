filenames = ['a.txt','b.txt','c.txt']
for file in filenames:
    f=open(file,'r')
    content=f.read()
    print(content)