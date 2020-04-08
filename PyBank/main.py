import os
import csv

budget_csv = os.path.join('..','resources','budget_data.csv')

csvreader = csv.reader(budget_csv , delimiter =',')

#read in the CSV file
with open('budget_data.csv','r') as csvfile:
    csvreader =csv.reader(csvfile, delimiter =',')   
    header_row=next(csvreader)
    prev_row=next(csvreader)
    total_month = 1
    total_profit = int(prev_row[1])
    total_changes =[]
    greatest_increase=["",-100000000]
    greatest_decrease=["",100000000]
    for eachline in csvreader:
        # print (eachline) 
        total_month=total_month+1
        total_profit=total_profit+int(eachline[1])
        change=int(eachline[1])-int(prev_row[1])
        total_changes.append(change)
        prev_row=eachline
        # if  Increase in Profits = highest
        if change > greatest_increase[1]:
            greatest_increase[0]=eachline[0]
            greatest_increase[1]=change
        # if  Decrease in Profits = loweast
        if change < greatest_decrease[1]:
            greatest_decrease[0]=eachline[0]
            greatest_decrease[1]=change

        # Print (Greatest Increase in Profits: date, amount)
        # if  Decrease in Profits = loweast
        # print (Greatest Decrease in Profits: date, amount)
# print (total_month)
# print(total_profit)
# print(sum(total_changes)/len(total_changes))
# # Print (Greatest Increase in Profits: date, amount)
# print (f"{greatest_increase[0]},${greatest_increase[1]}")

# # print (Greatest Decrease in Profits: date, amount)
# print (f"{greatest_decrease[0]},${greatest_decrease[1]}")
output=f"""output
==========================================
Total month: {total_month}
Total profit: ${total_profit}
Average change: ${sum(total_changes)/len(total_changes)}
Greatest increase: {greatest_increase[0]}, ${greatest_increase[1]}
Greatest_decrease: {greatest_decrease[0]}, ${greatest_decrease[1]}
"""
print (output)
with open("output.txt","w") as text_file:
    text_file.write (output)
   
