import csv

#----Open budget data for reading and skip header row ----
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
    months = []

    #calculate total months and net profit/losses over entire period
    #create a new list for each column of data
    for row in csv_reader:
        total_months += 1
        monthly_total += int(row[1])
        profitloss_list.append(row[1])
        months.append(row[0])
    
    #use range(len() to "iterate over numbers used as indices" in order to begin at index 1. 
    #source: https://www.kite.com/python/answers/how-to-use-range(len())-in-python#:~:text=Use%20range()%20and%20len,access%20the%20items%20in%20obj%20.
    for i in range(1, len(profitloss_list)):
        
        #calculate monthly change and store in monthly_change list
        monthly_change.append(int(profitloss_list[i]) - int(profitloss_list[i-1]))

        #calculate total average change
        average_change = sum(monthly_change) / len(monthly_change)
        greatest_increase = max(monthly_change)
        greatest_decrease = min(monthly_change)
    
    position_increase = monthly_change.index(greatest_increase) + 1
    position_decrease = monthly_change.index(greatest_decrease) + 1

    # ------ Printing to check calculations ------
    # print(total_months)
    # print(monthly_total)
    # print(months[position_increase])
    # print(months[position_decrease])
    # print(greatest_increase)
    # print(greatest_decrease)
    # print(average_change)

    #------ Final Output --------

    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${monthly_total}")
    print(f"Average Change: ${round(average_change, 2)}")
    print(f"Greatest Increase in Profits: {months[position_increase]} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {months[position_decrease]} (${greatest_decrease})")



