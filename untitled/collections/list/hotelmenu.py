starter=[
    [1,2,3,4],
    ['Veg Manurian','Masala Papad','Tomato Soup','Corn Soup'],
    [200,50,140,120]
]
veg=[
    [1,2,3,4,5],
    ['Paneer Masala','Veg Maratha','Veg Kolhapuri','Caju Curry ','Paneer Tikka'],
    [120,20,100,300,280]
]
nonveg=[
    [1,2,3,4,5,6,7,8],
    ['Chicken Masala','Mutton Korma','Tandoori Chicken','Hydrabadi Chicken Masala','Fish Fry','Sheek Kabab','Chilli Chicken','Mutton Curry'],
    [200,399,430,100,240,330,200,190]
]
bill=0
ono=0
order=[[],[]]
while(1):
    print('-------------------HOTEL PARADISE--------------------')
    print('Place New Order\n1:Starters\n2:Veg Menu\n3:Non-Veg Menu\n4:Exit')
    ch=int(input('Enter your choice : '))

    if(ch==1):
        print('----------------Starters----------------')
        print('No   Name        Price')
        for i in range(0,len(starter[0])):
            print(str(starter[0][i]) + ' : ' + str(starter[1][i]) + ' : ' + str(starter[2][i]))
        print('**press 0 to exit**')
        ono=int(input('enter dish no you want to order :'))
        if(ono in starter[0]):
            order[0].append(starter[1][ono-1])
            order[1].append(starter[2][ono-1])
        else:
            print('Invalid Dish no ..Please check..')

    elif(ch==2):
        print('----------------VEG MENU----------------')
        print('No   Name        Price')
        for i in range(0,5):
            print(str(veg[0][i]) + ' : ' + str(veg[1][i]) + ' : ' + str(veg[2][i]))
        print('**press 0 to exit**')
        ono = int(input('enter dish no you want to order :'))
        if(ono in veg[0]):
            order[0].append(veg[1][ono - 1])
            order[1].append(veg[2][ono - 1])
        else:
            print('Invalid Dish no ..Please check..')

    elif(ch==3):
        print('----------------NON-VEG MENU----------------')
        print('No   Name         Price')
        for i in range(0,len(nonveg[0])):
            print(str(nonveg[0][i])+' : '+str(nonveg[1][i])+' : '+str(nonveg[2][i]))
        print('**press 0 to exit**')
        ono = int(input('enter dish no you want to order :'))
        if(ono in nonveg[0]):
            order[0].append(nonveg[1][ono - 1])
            order[1].append(nonveg[2][ono - 1])
        else:
            print('Invalid Dish no ..Please check..')

    elif(ch==4):
        print('Thank you for visiting us..')
        break

    else:
        print('Invalid choice....')

    con=int(input('Do you want to place more order.....press 1'))
    if(con!=1):
        break
print('\n***********************************************************\n')
if(len(order[0])==0):
    print('No oreder received yet....')
else:
    print('------------------Your Order Is-----------------')
    print('   No   Name    Price   ')
    for i in range(0,len(order[0])):
        print(str(i+1)+' : '+str(order[0][i])+' : '+str(order[1][i]))
        bill+=order[1][i]
    print('------------------------------------------------')
    print('\nYour Total Bill Is : ',bill)
    print('\n-------------------------------------------------')
print('\n*************************************************************')