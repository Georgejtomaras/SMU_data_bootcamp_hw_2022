import os
import csv

# Set file path
csvpath = os.path.join( 'Resources', 'election_data.csv')
pathout = os.path.join( "analysis", "election_results.txt")

# Lists and variables to store data
candidates = []
votes = []
county = []
Charles = []
Diana = []
Raymon = []

#Extract Data from election_data.csv to create three columns: `Voter ID`, `County`, and `Candidate`
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header and loop through rows
    for row in csvreader:
        votes.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
        
    # The total number of votes cast
        voter_total = len(row [1])

    # A complete list of candidates who received votes and the total number of votes each candidate won.
        for can in candidates:
            if can == "charles":
                Charles.append(candidates)
                votes_Charles = len(Charles)
            elif can == "diana":
                Diana.append(candidates)
                votes_Diana = len(Diana)
            else:
                Raymon.append(candidates)
                votes_Raymon = len(Raymon)

    # The percentage of votes each candidate won.
    per_Charles = round(((votes_Charles / voter_total) * 100), 2)
    per_Diana = round(((votes_Diana / voter_total) * 100), 2)
    per_Raymon = round(((votes_Raymon / voter_total) * 100), 2)

    # The winner of the election based on popular vote.
    def winner(candidates):
        return max(set(candidates), key = candidates.count)




print("Election Results")
print("----------------------------")
print(f"Total votes:  {votes}")
print("----------------------------")
print(f"Charles Casper Stockham: %{per_Charles} ({votes_Charles})")
print(f"Diana Degette: %{per_Diana} ({votes_Diana})")
print(f"Raymon Anthony Doane: %{per_Raymon} ({votes_Raymon})")
print("----------------------------")
print(f"Winner: ({winner})")
print("----------------------------")

#  Export a text file with the results to Analysis folder.
with open(pathout, "w") as results:
    results.write("Election Results\n")
    results.write("----------------------------\n")
    results.write(f"Total votes:  {votes}\n")
    results.write("----------------------------\n")
    results.write(f"Charles Casper Stockham: %{per_Charles} ({votes_Charles})\n")
    results.write(f"Diana Degette: %{per_Diana} ({votes_Diana})\n")
    results.write(f"Raymon Anthony Doane: %{per_Raymon} ({votes_Raymon})\n")
    results.write("----------------------------\n")
    results.write(f"Winner: ({winner})\n")
    results.write("----------------------------\n")

    
