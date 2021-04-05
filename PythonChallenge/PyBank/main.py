#import budget data 
import os
import csv 

# Declare the Path to collect data from the Instructions folder
budget_data_csv = os.path.join("budget_data.csv")
pathout = os.path.join("budget_analysis.txt")

with open(budget_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
# Create empty lists to use when iterating through specific rows for variables as follow
    mcount = 0
    total = 0
    PreValue = 0
    revenue_change = 0
    Diff = 0
    DiffMax = 0
    DiffMin = 0
    
    print(f"Header: {csv_header}")               
    for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - PreValue
         #For financial analysis placeholder to track greatest increase in profits 
         if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month
         #For financial analysis placeholder to track greatest decrease in profits
         if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month

         PreValue = iAmount   
         # Get total months 
         mcount = mcount + 1
         total += int(Amount)

## Display the results as requested
# Print Statements
print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')
# Print the total number of months present in the dataset
print(f'Total Months : {mcount}')
#The total net amount of "Profit/Losses" over the entire period
print(f'Total: $ {total}')
# Print the average change in revenue
# The greatest increase in profit
print(f'Greatest Increase in Profits: {DiffMaxDate}  ($ {DiffMax})')
# The greatest decrease in profit
print(f'Greatest Decrease in Profits: {DiffMinDate}  ($ {DiffMin})')         

# output file to generate 

#Write to the text path
with open(pathout, "w") as file:
       
    file.write(f"Financial Analysis"+'\n')
    file.write(f"----------------------------"+'\n')
    file.write(f"Total Months: {mcount}")
    file.write(f"Total: $ {total}")
    file.write(f'Greatest Increase in Profits: {DiffMaxDate}  ($ {DiffMax})')
    file.write(f'Greatest Decrease in Profits: {DiffMinDate}  ($ {DiffMin})') 