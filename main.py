import excelfunctions as exf
from os.path import exists

TEMPDATAPATH = "data/tempdata.csv"

excelfilepath = ""
while(not exists(excelfilepath)):
    excelfilepath = input("What excel file do you want to edit? ")

exf.convert_to_csv(excelfilepath)

usercommand = ['empty']
commands = ["addrow", "search"]

while( not(usercommand[0].lower() in commands)):
    usercommand = input("What action? ").split()

    if usercommand[0].lower() == "help":
        print(commands)

exf.func_dict(usercommand[0], TEMPDATAPATH)

exf.convert_to_excel(TEMPDATAPATH)
