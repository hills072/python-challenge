import csv



with open("Resources/election_data.csv", "r") as election_data:
    csv_reader = csv.reader(election_data)

    next(csv_reader)
    
    total_votes = 0
    Khan = 0
    Correy = 0
    Li = 0
    OTooley = 0

    candidates = []

    for row in csv_reader:
        total_votes += 1
        candidates.append([row[2]])

        
    Khan = sum("Khan" in i for i in candidates)
    Correy = sum("Correy" in i for i in candidates)
    Li = sum("Li" in i for i in candidates)
    OTooley = sum("O'Tooley" in i for i in candidates)

    KhanPercent = (Khan / (Khan + Correy + Li + OTooley)) * 100
    CorreyPercent = (Correy / (Khan + Correy + Li + OTooley)) * 100
    LiPercent =  (Li / (Khan + Correy + Li + OTooley)) * 100
    OTooleyPercent = (OTooley / (Khan + Correy + Li + OTooley)) * 100
    
    print(f'{round(KhanPercent, 5)}%')

    print(f'{round(CorreyPercent, 5)}%')

    print(f'{round(LiPercent, 5)}%')

    print(f'{round(OTooleyPercent, 5)}%')

    # print(Khan)
    # print(Correy)
    # print(Li)
    # print(OTooley)

            
        
    

    # print(total_votes)
    
    
        
        
