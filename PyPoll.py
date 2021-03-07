#The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os
# Create a filename variable to a direct or indirect path to the file.
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # to do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)

    # Print each row in the csv file:
    for row in file_reader:
        #print(row)
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] += 1
    #print (candidate_votes)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = votes/total_votes*100
        if votes > winning_count and vote_percentage > winning_percentage:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
        f"-------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n"
        f"-------------------------------\n"
    )
    print(winning_candidate_summary)
