#create a script to analyze the financial records of your company.
#columns: Date and Profit/Losses

import os
#import datetime
import csv

PyBank_csv = os.path.join("..", "Resources", "budget_data.csv")

#calculate
#net_change = []
PL_change_total = []
greatest_increase = []
greatest_decrease = []
month_change = []
months_total = 0
total_net = 0

#def budget_data(budget):
    #date = str(budget[0])
    #profit_loss = int(budget[1])

with open(PyBank_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_reader)
    #print(f"Header: {csv_header}")
    
    for row in csv_reader:
        total_net += int(row[1])
        months_total = +1
        PL_change_total = round(int(row[1]) / 86, 2)
        greatest_increase = max(row[1])
        greatest_decrease = min(row[1])
        
    #total=[]
    #total = 0
    #total=sum(int([1]) for r in csv_reader)
    #print('Total:', total)
    print("Financial Analysis")
    print("--------------------------")
    months = len(csv_file.readlines())
    print('Total Months:', months)

    #print('Total Months:', months_total)
    print('Total: $',total_net)
    print('Average Change: $', PL_change_total)
    print('Greatest Increase in Profits: $', greatest_increase)
    print('Greatest Decrease in Profits: $', greatest_decrease)










#calculate each of the following values:

#the net total amount of "profit/losses" over the entire period
#the changes in "profit/losses" over the entire period
    #and then the average of those changes
#the greatest increase in profts (date and amount) over the entire period
#the greatest decrease in profits (date and amount) over the entire period

#final script should print the analysis to the terminal and export a text file with the results

