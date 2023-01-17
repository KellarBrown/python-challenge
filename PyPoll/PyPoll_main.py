# import csv dependency
import csv

# stores the file path into csvpath
csvpath = "Resources/election_data.csv"

# opens the file for reading
with open(csvpath) as csvfile:

    # reads and stores items separated by a comma 
    csvreader = csv.reader(csvfile,delimiter=',')

    # skips the header row and stores it
    csvheader = next(csvreader)

    # declared variables
    total_votes = 0
    distinct_candidates = []
    votes_per_candidate =[]
    percentage_of_total_votes = []

    # a for loop to iterate through rows in the file
    for row in csvreader:

        # calculates the total number of votes
        total_votes +=1
        
        # isolates each individual candidate and calculates the votes per candidate
        if row[2] not in distinct_candidates:
            distinct_candidates.append(row[2])
            index = distinct_candidates.index(row[2])
            votes_per_candidate.append(1)
        else:
            index = distinct_candidates.index(row[2])
            votes_per_candidate[index] += 1
    # a for loop to iterate through the votes per candidate and to calculate the total percentage based on those votes
    for i in votes_per_candidate:
        percentage_of_votes = round((i/total_votes)*100,3)
        percentage_of_total_votes.append(percentage_of_votes)           

    # captures the index of which candidate has the highest vote count
    index = votes_per_candidate.index(max(votes_per_candidate))
    
    # declares the winner based on the previously found index
    winner = distinct_candidates[index]

    # print statements
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for i in range(len(distinct_candidates)):
        print(f"{distinct_candidates[i]}: {percentage_of_total_votes[i]}% ({votes_per_candidate[i]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")   

# stores the path of the output text file into the variable "output"    
output = "Resources/election_data_analysis.txt"

# opens the file as writable
with open(output,'w') as fileoutput:

    # write statements to write the data to the output text file
    fileoutput.write("Election Results\n")
    fileoutput.write("-------------------------\n")
    fileoutput.write(f"Total Votes: {total_votes}\n")
    fileoutput.write("-------------------------\n")
    for i in range(len(distinct_candidates)):
        fileoutput.write(f"{distinct_candidates[i]}: {percentage_of_total_votes[i]}% ({votes_per_candidate[i]})\n")
    fileoutput.write("-------------------------\n")
    fileoutput.write(f"Winner: {winner}\n")
    fileoutput.write("-------------------------\n")   



