import csv

with open("Resources/election_data.csv", "r") as election_data:
    csv_reader = csv.reader(election_data)

    # remove header data from csv
    next(csv_reader)

    # create empty dictionary to store amount of votes per candidate

    Votes_per_candidate ={}

    # inititalize counter variable for total votes

    total_votes = 0

    # find total number of votes cast
    # count the votes for each candidate and put them into a dictionary 
    # as key = candidate, value = votes

    for row in csv_reader:
        
        total_votes += 1
        
        if row[2] in Votes_per_candidate.keys():
            Votes_per_candidate[row[2]] += 1
        else:
            Votes_per_candidate[row[2]] = 1

    print(f'Election Results')
    print("--------------------------")
    print(f'Total Votes: {total_votes}')
    print("--------------------------")
    
    for candidate in Votes_per_candidate:

        #get the total votes for each candidate and store it in votes
        votes = Votes_per_candidate.get(candidate)

        # calculate the percentage of votes won per candidate and output each candidate's
        # name along with percentage of votes won and total amount of votes per candidate
        percent = (Votes_per_candidate[candidate]) / (total_votes) * 100
        print(f'{candidate}: {percent:.3f}% ({votes})')

    # find winner by getting the name of the candidate with the highest vote count
    winner = max(Votes_per_candidate, key=Votes_per_candidate.get)
    print("--------------------------")
    print(f'Winner: {winner}')
    print("--------------------------")


# export output to text file
with open('Analysis/polldata.txt', 'w') as txt_file:

    txt_file.write(f'Election Results\n')
    txt_file.write("--------------------------\n")
    txt_file.write(f'Total Votes: {total_votes}\n')
    txt_file.write("--------------------------\n")
    for candidate in Votes_per_candidate:

        votes = Votes_per_candidate.get(candidate)

        percent = (Votes_per_candidate[candidate]) / (total_votes) * 100
        txt_file.write(f'{candidate}: {percent:.3f}% ({votes})\n')
    txt_file.write("--------------------------\n")
    txt_file.write(f'Winner: {winner}\n')
    txt_file.write("--------------------------\n")