import os
import csv

budget_csv = os.path.join("budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    months = []
    avglist = []
    profit_change = [0]
    total = 0
    totprof = 0
    str1 = ""
    str2 = ""

    for row in csvreader:
        avglist.append(int(row[1]))
        total += float(row[1])
        months.append(row[0])
    
    initial = 0
    for x in range(int(len(avglist)-1)):
        initial = (avglist[x+1]-avglist[x])
        profit_change.append(initial)

    for b in range(int(len(profit_change))):
        totprof += profit_change[b]
    
    avg = totprof / int(len(profit_change)-1)

    new_file = zip(months,avglist,profit_change)

    for c in new_file:
        if int(c[2]) == max(profit_change):
            str1 = str1 + str((c[0]))
    
    #why do i have to remake this zip file to get the calculation to work?
    new_file2 = zip(months,avglist,profit_change)
    for d in new_file2:
        if int(d[2]) == min(profit_change):
            str2 = str2 + str((d[0]))
    
    
print("-----------------------------------------------------------")
print("Total Months: " + str(len(months)))
print("Total: $" + str(total))
print("Average Change: $" + str(round(avg,2)))
print("Greatest Increase in Profits: " + str1 + " $" + str(max(profit_change)))
print('Greatest Decrease in Profits: ' + str2 + " $" + str(min(profit_change)))

final_file = ["Total Months: " + str(len(months)),"Total: $" + str(total),"Average Change: $" + str(round(avg,2)),
"Greatest Increase in Profits: " + str1 + " $" + str(max(profit_change)),'Greatest Decrease in Profits: ' + str2 + " $" + str(min(profit_change))]

output_file = os.path.join("Final_Analysis.txt")

with open(output_file, "w") as datafile:
    for s in final_file:
        datafile.write("%s\n" % s)