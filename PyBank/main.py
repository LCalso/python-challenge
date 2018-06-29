import os 
import csv

budgetCSV = 'budget_data.csv'

Total_Months = 0
Total_Revenue = 0
Previous_Revenue = 0
Avg_Revenue_Change = 0
Greatest_Rev_Inc_Date = "Date1"
Greatest_Rev_Inc_Amt = 0
Greatest_Rev_Dec_Date = "Date2"
Greatest_Rev_Dec_Amt = 0
Total_Revenue_Change = 0
 
with open(budgetCSV,'r') as csvfile:
    actualdata = csv.reader(csvfile, delimiter=",")
    headerrow = next(actualdata)

    for row in actualdata:
        Total_Revenue = Total_Revenue + int(row[1])
        Total_Months = Total_Months +1
        Revenue_Increase = int(row[1]) - Previous_Revenue
        Total_Revenue_Change = Total_Revenue_Change + Revenue_Increase
        Previous_Revenue =  int(row[1])
        
        if(Revenue_Increase > Greatest_Rev_Inc_Amt):
           Greatest_Rev_Inc_Amt = Revenue_Increase
           Greatest_Rev_Inc_Date = row[0]

        if(Revenue_Increase < Greatest_Rev_Dec_Amt):
           Greatest_Rev_Dec_Amt = Revenue_Increase 
           Greatest_Rev_Dec_Date = row[0]

Avg_Revenue_Change = round(Total_Revenue_Change/Total_Months, 2)

outputpath = ("Results.txt")
    
lines = []
    
resultsfile = open(outputpath, "w")
lines.append("Financial Analysis")
lines.append("----------------------------")
lines.append("Total Months: "+str(Total_Months))
lines.append("Total Revenue: $" +str(Total_Revenue))
lines.append("Average Revenue Change: $"+str(Avg_Revenue_Change))
lines.append("Greatest Increase in Revenue: "+Greatest_Rev_Inc_Date + " ($" + str(Greatest_Rev_Inc_Amt) + ")")
lines.append("Greatest Decrease in Revenue: "+Greatest_Rev_Dec_Date + " ($" + str(Greatest_Rev_Dec_Amt) + ")")

for line in lines:
    print (line)
resultsfile.close()