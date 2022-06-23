import csv
import os

csvpath = os.path.join("Resources", "election_data.csv")

print(csvpath)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    
    vote_counter=0
    pre_name = '' 
    can_counter = 0
    can_vote_counter = 1
    canlist=[]
    candict={}
    candict1={}
    
    for row in csvreader:
        vote_counter = vote_counter+1
        
        can_name = row[2]
        
        while can_name not in canlist:
            canlist.insert(can_counter,can_name)
            can_counter = can_counter + 1
            candict[can_name]=0
          
        if row[2] in candict:
            candict[row[2]] = candict[row[2]] + 1
        else:
            print(row[2])
            
        vote_per = round((candict[row[2]]/vote_counter)*100,3)
        candict1[row[2]] = str(vote_per) + "%" + "  " + "(" + str(candict[row[2]]) + ")"
        
winner = max(candict,key=candict.get)            

print ("Election Result")
print("-----------------------")
print (f"Total Votes : {vote_counter}")
print("-----------------------")
for i in candict1:
    print(f"{i} : {candict1[i]}")
print("-----------------------")
print(f"Winner : {winner}")

