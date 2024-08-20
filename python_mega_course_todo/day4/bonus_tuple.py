#data mutability
filenames = ["1.file.txt","2.info.txt","3.report.txt"]
for f in filenames:
    f = f.replace('.','_',1)
    print(f)

