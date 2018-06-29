import os
import csv

ElectionCSV = 'election_data.csv'

votes = 0
candidates = []
vote_count = {}
vote_percent = {}

with open(ElectionCSV, newline="") as csvfile:
    actualdata = csv.reader(csvfile, delimiter=",")
    
    for row in actualdata:
        votes = votes + 1        

        if row[2] not in candidates and row[2] not in "Candidate":
            candidates.append(row[2])
            vote_count[row[2]] = 1
        elif row[2] in candidates and row[2] not in "Candidate":
            vote_count[row[2]] = vote_count[row[2]] + 1

    for key, value in vote_count.items():
        vote_percent[key] = str(round(((value/votes)*100),3)) + "% ("+str(value) + ")"

    maxi = max(vote_count.keys(), key=(lambda k: vote_count[k]))    
    
    space = "-------------------------------"
    results1 = (
        "Election Results" + '\n' + space + '\n' + "Total Votes: "+ str(votes)+ '\n' + space + '\n')
    results2 = (
        space + '\n'
        "Winner: "+ str(maxi)+ '\n' + space + '\n')
   
    print(results1)
    for key, val in vote_percent.items():
        print(key, ": ", val)
    print(results2)
    
    f = open("Election_results.txt", "w")

    f.write(results1)
    for key, val in vote_percent.items():
         f.write((key + ": " + val)+ '\n')
    f.write(results2)
    
    f.close()
