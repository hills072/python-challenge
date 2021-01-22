import csv

with open('budget_data.csv', 'r') as budget_data:
    csv_reader = csv.reader(budget_data)

    next(csv_reader)

    total_months = 0

    for row in csv_reader:
        total_months += 1
    
    print (total_months)

    # monthly_total = 0

    # for row in csv_reader:
    #     monthly_total += int(row[1])
        
    # print(monthly_total)


    # for line in csv_reader:
    #     print(line)


