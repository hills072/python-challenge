import csv

with open("Resources/election_data.csv", "r") as election_data:
    csv_reader = csv.reader(election_data)

    next(csv_reader)
    
    total_votes = 0

    candidates_column = []

    for row in csv_reader:
        total_votes += 1
        candidates_column.append([row[2]])

    def get_unique_names(candidates_column):
        
        unique_names_list = []
        
        for name in candidates_column:
            if name in unique_names_list:
                continue
            else:
                unique_names_list.append(name)
        return unique_names_list

    unique_names = [get_unique_names(candidates_column)]
    print(unique_names)

    for name in unique_names:
        candidates_column.count()


    
    
    # list.count(candidates_column("Khan"))
        
    


    
        
    # Khan_tot = sum("Khan" in i for i in candidates_column)
    # Correy_tot = sum("Correy" in i for i in candidates_column)
    # Li_tot = sum("Li" in i for i in candidates_column)
    # OTooley_tot = sum("O'Tooley" in i for i in candidates_column)

    # Pop_vote_summary = {"Khan": Khan_tot, "Correy": Correy_tot, "Li": Li_tot, "O'Tooley": OTooley_tot}

    # winner = max(Pop_vote_summary, key=Pop_vote_summary.get)

    # KhanPercent = (Khan_tot / (Khan_tot + Correy_tot + Li_tot + OTooley_tot)) * 100
    # CorreyPercent = (Correy_tot / (Khan_tot + Correy_tot + Li_tot + OTooley_tot)) * 100
    # LiPercent =  (Li_tot / (Khan_tot + Correy_tot + Li_tot + OTooley_tot)) * 100
    # OTooleyPercent = (OTooley_tot / (Khan_tot + Correy_tot + Li_tot + OTooley_tot)) * 100

    
    # print("Election Rresults")
    # print("--------------------------")
    # print(f"Total Votes: {total_votes}")
    # print("--------------------------")
    # print(f"Khan: {KhanPercent:.3f}% ({Khan_tot})")
    # print(f"Correy: {CorreyPercent:.3f}% ({Correy_tot})")
    # print(f"Li: {LiPercent:.3f}% ({Li_tot})")
    # print(f"O'Tooley: {OTooleyPercent:.3f}% ({OTooley_tot})")
    # print("--------------------------") 
    # print(f"Winner: {winner}")
    # print("--------------------------")      


# print(winner)
    # print(Pop_vote_summary)
    # print(f'{round(KhanPercent, 5)}%')
    # print(f'{round(CorreyPercent, 5)}%')
    # print(f'{round(LiPercent, 5)}%')
    # print(f'{round(OTooleyPercent, 5)}%')
    # print(Khan)
    # print(Correy)
    # print(Li)
    # print(OTooley)
    # print(total_votes)
