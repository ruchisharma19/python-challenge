import csv
import os

csvpath = os.path.join('Resources','budget_data.csv')

print(csvpath)


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    
    rowcount=0
    total=0
    preval=0
    diffdict = {}
    
    for row in csvreader:
        rowcount = rowcount+1
 
        total = total + int(row[1])
        
        change = float(row[1]) - float(preval)
        preval = row[1]
        
        mon=row[0]
             
        if rowcount == 1:
            change = 0
    
            strtval = row[1]

        diffdict[mon] = change  
      
    maxprofit_mon = max(diffdict,key=diffdict.get) 
    maxloss_mon = min(diffdict,key=diffdict.get)
    
    
    average = round((float(preval) - float(strtval))/(rowcount - 1),2)
    
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months :  {rowcount}")
    print(f"Total : ${total}")
    print(f"Average Change : ${average}")
    print(f"Greatest Increase in Profits : {maxprofit_mon} (${diffdict[maxprofit_mon]})")
    print(f"Greatest Decrease in Profits : {maxloss_mon} (${diffdict[maxloss_mon]})")
