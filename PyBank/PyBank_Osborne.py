# import modules
import os
import csv

# open and read csv file
csvpath = os.path.join('Resources', 'budget_data.csv')
output = os.path.join('Resources', 'budget_analysis.txt')

#total month needs to be set to 0 to I can count
totalMonth = 0
totalRevenue = 0
previousRevenue = 0
revenue_change = 0
revenue_change_list = []
month_of_change = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 99999999999]

#Read the budget_data.csv file
with open(csvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter =",")
   header = next(csvreader)

#I need to loop through the data to collect the answers
   for row in csvreader:

       #Totaling
        totalMonth = totalMonth + 1
        totalRevenue = totalRevenue + int(row[1])

#changes of revenue calculations
        revenue_change = int(row[1]) - previousRevenue
        revenue_change_list.append(revenue_change)
        previousRevenue = int(row[1])
        month_of_change = month_of_change + [row[0]]

           #Greatest Increase value
        if (revenue_change > greatestIncrease[1]):
            greatestIncrease[1] = revenue_change
            greatestIncrease[0] = row[0]

        if (revenue_change < greatestDecrease[1]):
            greatestDecrease[0] = row[0]
            greatestDecrease[1] = revenue_change
        
# calculate the average revenue outside of the loop
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)


output = (
    f"Total Months: {totalMonth}\n"
    f"Total Revenue: {totalRevenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatestIncrease[0]} ${greatestIncrease[1]}\n"
    f"Greatest Decrease in Revenue: {greatestDecrease[0]} ${greatestDecrease[1]}\n"
)

print(output)

#print the outcomes/##prints to file
output_file = os.path.join('Resources', 'financial_analysis.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines("Financial Analysis\n")
    txtfile.writelines("--------------------\n")
    txtfile.writelines(output)
        #prints file to terminal
    with open(output_file, 'r') as readfile:

        print(readfile.read())