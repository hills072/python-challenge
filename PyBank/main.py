import os
import csv

with open('budget_data.csv', 'r') as budget_data:
    csv_reader = csv.reader(budget_data)

    next(csv_reader)

    #initialize counter variables
    total_months = 0
    monthly_total = 0

    #create empty lists to store data
    monthly_change = []
    profitloss_list = []
    monthly_change = []

    #calculate total months and net profit/losses over entire period
    for row in csv_reader:
        total_months += 1
        monthly_total += int(row[1])
        profitloss_list.append(row[1])
    
    print(total_months)
    print(monthly_total)
    
    #use range(len() to "iterate over numbers used as indices" in order to begin at index 1. 
    #source: https://www.kite.com/python/answers/how-to-use-range(len())-in-python#:~:text=Use%20range()%20and%20len,access%20the%20items%20in%20obj%20.
    for i in range(1, len(profitloss_list)):
        
        #calculate monthly change
        monthly_change.append(int(profitloss_list[i]) - int(profitloss_list[i-1]))

        #calculate total average change
        average_change = sum(monthly_change) / len(monthly_change)
        greatest_increase = max(monthly_change)
        greatest_decrease = min(monthly_change)
    

    print(average_change)