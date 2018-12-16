import os
import csv

Amounts = []
Dates = []
TotalMonths = 0
TotalProfitLosses = 0
MaxProfitLosses = 0
MinProfitLosses = 0

with open('budget_csv.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    for row in csv_reader:
        if line > 0:
            Dates.append(row[0])
            Amounts.append(int(row[1]))
        line = line+1

TotalMonths = len(Dates)
TotalProfitLosses = sum(Amounts)
Average = TotalProfitLosses/TotalMonths

MaxProfitLosses = max(Amounts)
MinProfitLosses = min(Amounts)

IndexMax = Amounts.index(MaxProfitLosses)
IndexMin = Amounts.index(MinProfitLosses)

MaxMonth = Dates[IndexMax]
MinMonth = Dates[IndexMin]


budget_output = open('budget_output.txt', 'w')

print('Financial Analysis')
budget_output.write('Financial Analysis'+'\n')

print('------------------------------------------')
budget_output.write('------------------------------------------'+'\n')

print('Total Months: ', TotalMonths)
budget_output.write('Total Months: '+str(TotalMonths)+'\n')

print('Total        :$', TotalProfitLosses)
budget_output.write('Total        :$'+str(TotalProfitLosses)+'\n')

print('Greatest Increase In Profits:',MaxMonth+'('+'$'+str(MaxProfitLosses)+')')
budget_output.write('Greatest Increase In Profits:'+MaxMonth+'('+'$'+str(MaxProfitLosses)+')'+'\n')

print('Greatest Decrease In Profits:',MinMonth+'('+'$'+str(MinProfitLosses)+')')
budget_output.write('Greatest Decrease In Profits:'+MinMonth+'('+'$'+str(MinProfitLosses)+')'+'\n')

budget_output.close()