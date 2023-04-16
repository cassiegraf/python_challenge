#create a script to analyze the financial records of your company.
#columns: Date and Profit/Losses

import os
#import datetime
import csv

PyBank_csv = os.path.join("..", "Resources", "budget_data.csv")


def budget_data(budget):
    date = str(budget[0])
    profit_loss = int(budget[1])

    for date in csv_reader:
        print(budget_data)


with open(PyBank_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #csv_header = next(csv_reader)
    #print(f"Header: {csv_header}")


    print("Financial Analysis")
    print("--------------------------")
    
    months = len(csv_file.readlines())
    print('Total Months:', months)










#calculate each of the following values:
#the total number of months included in the dataset




#the net total amount of "profit/losses" over the entire period
#the changes in "profit/losses" over the entire period
    #and then the average of those changes
#the greatest increase in profts (date and amount) over the entire period
#the greatest decrease in profits (date and amount) over the entire period

#final script should print the analysis to the terminal and export a text file with the results

