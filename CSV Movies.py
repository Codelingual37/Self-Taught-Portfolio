import csv

list = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("C:\\Users\\danj9\\Desktop\\test.csv", "w+") as x:
    for i in list:
        write = csv.writer(x, delimiter=",")
        write.writerow(i)
        