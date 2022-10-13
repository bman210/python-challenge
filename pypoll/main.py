import os
import csv

election_csv = os.path.join("election_data.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    votes = []
    candidates = []
    cand_choice = []
    charles_count = 0
    diana_count = 0
    raymond_count = 0

    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])
    
    for c in range(int(len(candidates))):
        if str(candidates[c]) in cand_choice:
            pass
        else:
            cand_choice.append(str(candidates[c]))
    
    for q in range(int(len(candidates))):
        if candidates[q] == cand_choice[0]:
            charles_count = charles_count + 1
        elif candidates[q] == cand_choice[1]:
            diana_count = diana_count + 1
        else:
            raymond_count = raymond_count + 1

print("Election Results")

print("-----------------------------------")

print("Total Votes: " + str(len(votes)))
print("")
print(f'{cand_choice[0]}: {round(charles_count/int(len(candidates))*100,3)}% ({charles_count})')
print("")
print(f'{cand_choice[1]}: {round(diana_count/int(len(candidates))*100,3)}% ({diana_count})')
print("")
print(f'{cand_choice[2]}: {round(raymond_count/int(len(candidates))*100,3)}% ({raymond_count})')
print("")
print("-----------------------------------")
print(f'Winner : {cand_choice[1]}')

final_file = ["Total Votes: " + str(len(votes)), f'{cand_choice[0]}: {round(charles_count/int(len(candidates))*100,3)}% ({charles_count})', 
f'{cand_choice[1]}: {round(diana_count/int(len(candidates))*100,3)}% ({diana_count})', 
f'{cand_choice[2]}: {round(raymond_count/int(len(candidates))*100,3)}% ({raymond_count})',f'Winner : {cand_choice[1]}']

output_file = os.path.join("Final_Analysis.txt")

with open(output_file, "w") as datafile:
    for s in final_file:
        datafile.write("%s\n" % s)