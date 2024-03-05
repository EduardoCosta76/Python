'''Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1 '''

bill = 0
print('''Welcome to Python Pizza place, please, choose one of the below sizes: 
1 - Small Pizza (S): $15 
2 - Medium Pizza (M): 20
3 - Large Pizza (L): 25''')
size = int(input('Which size would you like? '))

if size == 1:
    bill = bill + 15
elif size == 2:
    bill = bill + 20
else:
    bill = bill + 25
add_pepperoni = str(input('Would you like to add some pepperoni? Y or N? ')).strip().upper()
if add_pepperoni == 'Y':
    # print('Okay')
    if size == 1:
        bill = bill + 2
    elif size == 2:
        bill = bill + 3
    elif size == 3:
        bill = bill + 3
add_cheese = str(input('Would you like to add some extra cheese on any pizza? Y or N? ')).strip().upper()
if add_cheese == 'Y':
    # print('Okay')
    bill = bill + 1
print('Your final bill is ${:.2f}'.format(bill))


