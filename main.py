import excelfunctions as exf

exf.convert_to_csv("data/expenditure.xlsx")
exf.add_entry("data/tempdata.csv")
exf.convert_to_excel("data/tempdata.csv")
