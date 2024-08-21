contents = ["fhusfhohfnvioegjriogj ioncdoifij fnfjjn",
            "dbewirerf ufgid fheifjeifjdi fdijf",
            "wsqshiufheuifh jif fnivnrjln vfovnoii fnioj"]
filenames = ["file.txt","info.txt","content.txt"]

for content,filename in zip(contents,filenames):
    f1 = open(filename,'w')
    f1.write(content)


