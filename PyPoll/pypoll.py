# Import Needed Module
import csv

# Set Filepath
csvpath = "PyPoll/Resources/election_data.csv"

# Create initial Variables
vote_count = 0
cand_dict = {}

#CSV using UTF-8 encode 
with open(csvpath, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Read CSV
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read Row/Count vote
    for row in csvreader:
        vote_count += 1

        #Add Dictionary
        row_cand = row[2]
        if row_cand in cand_dict.keys():
            cand_dict[row_cand] +=1
        else:
            cand_dict[row_cand] = 1

#Create TXT Output
output = f"""Election Results
-----------------------------
Total Votes: {vote_count}
-----------------------------\n"""

#New variables
max_c = ""
max_v = 0

for candidate in cand_dict.keys():
    votes = cand_dict[candidate]
    perc = 100 * (votes / vote_count)
    line = f"{candidate}: {round(perc, 3)}% ({votes})\n"
    output += line

    #Winner
    if votes > max_v:
        max_c = candidate
        max_v = votes

last_line = f"""-------------------------
Winner: {max_c}
-------------------------"""
output += last_line
print(output) #For printing in terminal 

with (open("PyPoll_Results.txt", "w") as f):
    f.write(output)