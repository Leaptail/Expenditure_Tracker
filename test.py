import excelfunctions as exf
import pandas
from csv import writer

test_file = pandas.read_excel("data/expenditure.xlsx")
test_csv = pandas.read_csv("data/tempdata.csv")

#print(test_csv[test_csv["Name"]])

for col in test_csv:
    print(col)

# print(test_csv)
# print(test_csv.head())
# print(test_file.info())