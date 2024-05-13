# Import Needed Module
import csv

# Set Filepath
csvpath = "PyBank/Resources/budget_data.csv"

# Create Variables 
month_count = 0
tot_prof = 0
last_profit = 0
changes = []
month_changes = []


# Open CSV using UTF-8 (Standard code from comic book activity)
with open(csvpath, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Address Header 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read row and columns
    for row in csvreader:
        # Count, [1] grabs needed amount 
        month_count = month_count + 1
        tot_prof = tot_prof + int(row [1])

        # Profit Math and Append list. Address Cell C2 (empty)

        if (month_count == 1):
            last_profit = int(row[1])
        else: 
            change = int(row[1]) - last_profit
            changes.append(change)
            month_changes.append(row[0])

            # Prevent issues with a reset
            last_profit = int(row[1])
# Had to move variables from the top to here because of a div 0 error

avg_change = sum(changes) / len(changes)
max_change = max(changes)
max_month_indx = changes.index(max_change)
max_month = month_changes[max_month_indx]
min_change = min(changes)
min_month_indx = changes.index(min_change)
min_month = month_changes[min_month_indx]
   
    #  Create and Send to Txt file (assisted by Xpert)
    
kpi_data = {
        "Total Months" : month_count,
        "Total Profit" : tot_prof,
        "Average Change" : avg_change,
        "Greatest Increase in Profit" : [max_month, max_change],
        "Greatest Decrease in Profit" : [min_month, min_change]
    } 
print(kpi_data) #For terminal printing 

with open("PyBank_Report.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    
    for kpi, value in kpi_data.items():
        file.write(f"{kpi}: {value}\n")

print("KPIs sent to PyBank_Report.txt")