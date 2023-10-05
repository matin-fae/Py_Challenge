import os
import csv

max_month = ""
min_month = ""
average_profit = 0
total_change = 0
total_amount = 0
total_months = 0
budget_data = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    last_change = None
    changes = []

    for row in csv_reader:
        total_months += 1
        month = str(row[0])
        amount = int(row[1])
        total_amount += amount
        
        if last_change != None:
            change = amount - last_change
            changes.append(change)
            if change == max(changes):
                max_month=month
            if change == min(changes):
                min_month=month
            
        last_change = amount

average_profit = sum(changes) / len(changes)        

budget_output = (
    f"Budget Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Amount: ${total_amount:,}\n"
    f"Average Change: ${average_profit:.2f}\n" 
    f"Greatest Increase: ${max(changes):,}, in {max_month}\n"
    f"Greatest Decrease: ${min(changes):,}, in {min_month}\n")

print(budget_output)
with open("budget_data.txt", "w") as txt_file:
    txt_file.write(budget_output)

#how add corresponding moth?
#
#   .-"""""""---,.               n,                                      ..--------..
#   \-          ,,'''-..      n   '\.                ,.n           ..--''           )
#    \-     . .,;))     ''-,   \     ''.. .'"'. .,-''    .n   ..-''   (( o         _/
#     \- ' ''''':'          ''-.'"|'--_  '     '  ,.--'''..-''         ' ' ' - .  _/
#      \-                       ''->.  \'  ,--. '/' >..''                        _/
#       \                     (,       /  /.  .\ \ ''    ,)                     ./
#        ''.    .  ..         ')          \ .. /         ('          ..       ./
#           ''-... . ._ .__         .''.  //..\\  ,'.            __ _ _,__.--'
#               /' ((    ..'' ' ' '-'  6  \/__\/  ' '- - -' ' ',''   - '\
#              '(.  6,    '..          /.   ''  .'          ,,'     ) )  )
#               '\  \'C_,_   ==,      / '_      _|\       ,'', ,,_.;-' _/
#                 '._ ,   ')   E     /'|_ ')()('_' \     C  ,I'''  _.-'
#                    ''''''\ (('   ,/  ''  (()) ''  '-._ _ __---'''
#                           '' '' '    '==='()'=='
#                                      '(       )'    
#        Acherontia atropos            '6        '
#        (Totenkopfschwaermer,          \       /
#        Death's Head Hawk-moth,        '       '
#        P"a"akallokiit"aj"a)           '       '
#                                       '      '
#                                        '    '
#                                         '..'