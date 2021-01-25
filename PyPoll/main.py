import csv
from collections import Counter

with open("Resources/election_data.csv", "r") as election_data:
    csv_reader = csv.reader(election_data)

    next(csv_reader)
    
    total_votes = 0

    Votes_per_candidate ={}
    candidates_column = []
    unique_names = []
    candidate = 0
    percent = 0
    votes = 0

    for row in csv_reader:
        
        total_votes += 1
        candidates_column.append(row[2])
        
        if row[2] in Votes_per_candidate.keys():
            Votes_per_candidate[row[2]] += 1
        else:
            Votes_per_candidate[row[2]] = 1

    print(f'Election Results')
    print("--------------------------")
    print(f'Total Votes: {total_votes}')
    print("--------------------------")


    for name in candidates_column:

        if name not in unique_names:
            unique_names.append(name)
    
    for candidate in Votes_per_candidate:

        votes = Votes_per_candidate.get(candidate)

        percent = (Votes_per_candidate[candidate]) / (total_votes) * 100
        print(f'{candidate}: {percent:.3f}% ({votes})')

    winner = max(Votes_per_candidate, key=Votes_per_candidate.get)
    print("--------------------------")
    print(f'Winner: {winner}')
    print("--------------------------")
    
