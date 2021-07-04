a=[]
n=int(input('enter no of values you want '))
print('enter values:')
for i in range(n):
    val=int(input(str(i+1)+' NO : '))
    a.append(val)
print('List is :',a)

while(1):
    print('---------------LIST MENU---------------')
    print('1:Insert \n2:Search \n3:Delete \n4:Reverse\n5:Sort \n6:Occurance\n7:Delete all')
    ch=int(input('enter your choice :'))

    if(ch==1):
        val=int(input('Enter element to insert '))
        ind=int(input('enter index '))
        a.insert(ind,val)
        print('List is :',a)

    elif(ch==2):
        val = int(input('Enter element to search '))
        if (val not in a):
            print(str(val) + ' not present in list')
        else:
            print('value found at index :',a.index(val))

    elif(ch==3):
        val = int(input('Enter element to Delete '))
        if (val not in a):
            print(str(val) + ' not present in list')
        else:
            a.remove(val)
        print('List is :', a)

    elif(ch==4):
        a.reverse()
        print(a)

    elif(ch==5):
        a.sort();
        print(a)

    elif(ch==6):
        n=int(input('enter no to check occurrance '))
        print(a.count(n))

    elif(ch==7):
        a.clear()
        print(a)

    else:
        print('Invalid choice ..')

    con=int(input('Do you want to continue....press 1...'))
    if(con!=1):
        break