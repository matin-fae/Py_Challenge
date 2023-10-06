import os
import csv

#setting up variables
votes_file = os.path.join("Resources" , "election_data.csv")
total_votes = 0
candidates = []
votes = {}

#reading csv file
with open(votes_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    #looping through rows
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]    
        #id = row[0]
        #county = row[1]

        #appending dict to count votes per candidate
        if candidate not in candidates:
            candidates.append(candidate)
            votes[candidate] = 0 
        votes[candidate] = votes[candidate] + 1

#output
votes_output = "Election Results\n"
votes_output +="-------------------------\n"
votes_output +=(f"Total Votes:  {total_votes:,}\n")  
votes_output +="-------------------------\n"
for candidate in votes:
    perc = (votes[candidate] / total_votes) *100
    votes_output +=(f"{candidate} : {perc:.2f}% / {votes[candidate]:,} Votes\n")
votes_output +="-------------------------\n"
winner = max(votes, key = votes.get)
votes_output +=(f"!Winner!: {winner}")

print(votes_output)

#save to file
with open("Analysis/votes_data.txt", "w") as txt_file:
    txt_file.write(votes_output)


#1 count rows with "for" loop DONE
#2 list of candidates using ".unique" DONE
#3 total votes for unique candidate DONE
#4 candidate votes (line3) / total count(line1) 'for percentage' DONE
#5 max candidate total DONE

