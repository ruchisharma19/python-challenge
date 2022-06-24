import csv
import os

csvpath = os.path.join('Resources','budget_data.csv')
outpath = os.path.join('Analysis','financial_analysis.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    
    rowcount=0
    total=0
    preval=0
    diffdict = {}
    sno_list = []
    yrmon_list = []
    profitloss_list = []
    cummttl_list = []
    incdec_list = []
     
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

        sno_list.append(rowcount)
        yrmon_list.append(mon)
        profitloss_list.append(row[1])
        cummttl_list.append(total)
        incdec_list.append(change)

outcsv=zip(sno_list,yrmon_list,profitloss_list,cummttl_list,incdec_list)

with open(outpath, 'w') as outfile:
    csvwriter = csv.writer(outfile)
    csvwriter.writerow(['SNO','Year Month','Profit/Loss','Cummulative Total','Increase/Decrease'])

    for rows in outcsv:

        csvwriter.writerow(rows)            
            
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
