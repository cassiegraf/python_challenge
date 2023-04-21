#create a script to analyze the financial records of your company.
#columns: Date and Profit/Losses

import os
#import datetime
import csv

PyBank_csv = os.path.join("..", "Resources", "budget_data.csv")

#calculate
#net_change = []
PL_change_total = []
PL_change = 0
PL_change_total_total = []
PL_change_final = -706444
#average_change =[]
greatest_increase = []
greatest_decrease = []
month_change = []
months_total = 0
total_net = 0
starting_value = 1088983


#Total Months - Doing a split in the first column, and separating them into its individual columns
#Net total amount of Profit/Losses - Aggregating the values to get a total number
#Changes in Profit/Losses - Aggregating the differences between the values, and then averaging those changes.
#Greatest increase in profits - Looking for the highest value of profits
#Greatest decrease in profits - Looking for the lowest value of profits.

with open(PyBank_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_reader)
    #print(f"Header: {csv_header}")
    
    for row in csv_reader:
        total_net += int(row[1])
        months_total = months_total + 1
        PL_change_total = int(row[1]) - starting_value
        starting_value = int(row[1])
        PL_change += PL_change_total 
        PL_change_total_total = round(PL_change_final / 85, 2)


        """PL_change_total = round(int(row[1]) / months_total, 2)
        
        greatest_decrease = min(row[1])"""
        print(greatest_increase)

#try this for reading lines to get greatest increase/decrease
    """line = csv_reader.readline()

    line_before=None
    line_after=None
while line:
    print(line)
    if line_before is None:
        line_before = line

    if line_after is None:
        line_before=line

    if line !=line_before:
        line_after=line

        ###do logic here###

    line=budget_data.readline()

#OR try storing every line in a dictionary/list and compare them later"""


    #total=[]
    #total = 0
    #total=sum(int([1]) for r in csv_reader)
    #print('Total:', total)
    print("Financial Analysis")
    print("--------------------------")
    months = len(csv_file.readlines())
    print('Total Months:', months_total)

    #print('Total Months:', months_total)
    print('Total: $',total_net)
    print('Average Change: $', PL_change_total_total)
    print('Greatest Increase in Profits: $', greatest_increase)
    print('Greatest Decrease in Profits: $', greatest_decrease)


output_file = os.path.join("PyBank_output.csv")

with open(output_file, "w") as PyBankFile:
    writer = csv.writer(PyBankFile)

    writer.writerow(["Total Months", "Total", "Average Change", "Greatest Increase in Profits", "Greatest Decrease in Profits"])
    writer.writerow(["86", "$ 22564198", "$ 4448.13", "$ 9", "$ 2"])

#calculate each of the following values:

#the net total amount of "profit/losses" over the entire period
#the changes in "profit/losses" over the entire period
    #and then the average of those changes
#the greatest increase in profts (date and amount) over the entire period
#the greatest decrease in profits (date and amount) over the entire period

#final script should print the analysis to the terminal and export a text file with the results

