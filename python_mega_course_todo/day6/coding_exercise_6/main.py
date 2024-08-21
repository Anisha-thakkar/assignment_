filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for file in filenames:
    f1=open(file,'w')
    f1.write('Hello')