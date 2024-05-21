import pandas
from csv import writer

def convert_to_csv(f):
    
    expenditure_file = pandas.read_excel(f)

    expenditure_file.to_csv("data/tempdata.csv",
                        index = None,
                        header = True)

    #print(expenditure_file)

def convert_to_excel(f):

    expenditure_file = pandas.read_csv("data/tempdata.csv")

    expenditure_file.to_excel("data/expenditure2.xlsx",
                            index = None,
                            header = True)
    
def add_entry(f):
    column_names = ["Name", "Type", "Price", "Sales Tax"]
    userinput = [0]
    while len(userinput) != 4:
        userinput = input("New Entry: (name,type,price,tax)\n").split()
    #sale = (float(input[2])*float(input[3]))
    #userinput.append(str(sale))
    
    with open(f, 'a') as f_object:
        object = writer(f_object)
        object.writerow(userinput)
        f_object.close()
    
    #df = pandas.DataFrame(pandas.read_csv("data/tempdata.csv"))
    #userinput = pandas.DataFrame(userinput, columns = column_names)
    #userinput = pandas.concat([userinput ]), ignore_index = True)
    #userinput.to_csv(f, mode = "a", index = False, header = False)


