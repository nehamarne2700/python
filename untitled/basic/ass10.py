
while(1):
    print('------------------MENU-------------------')
    print('\n1:Fator\n2:Factorial\n3:Prime No\n4:Reverse No\n5:Sum of digits')
    print('6:Armstrong no\n7:Palindrome No\n8:Power\n9:Fibbonacci Series\n10:Postive/Negative')
    choice=int(input('enter your choice'))

    if(choice==1):
        print('--------------FATOR--------------')
        num=int(input('Enter a Number '))
        print('Factor of '+str(num)+' are :')
        for i in range(1,(num//2)+1):
            if(num%i==0):
                print('',i)

    elif(choice==2):
        print('--------------FAcTORIAL------------')
        num=int(input('Enter a Number '))
        f=1
        for i in range(1,num+1):
            f=f*i
        print('Factorial of '+str(num)+' is '+str(f))

    elif (choice == 3):
        print('--------------PRIME------------')
        num = int(input('Enter a Number '))
        flag=1
        for i in range(2,(num//2)+1):
            if(num%i==0):
                flag=0
                break
        if(flag==1):
            print(str(num)+' is Prime no')
        else:
            print(str(num)+' is not a Prime no')

    elif (choice == 4):
        print('--------------Reverse------------')
        num = int(input('Enter a Number '))
        new=num
        rem=0
        rev=0
        while(new!=0):
            rem=new%10
            rev=rev*10+rem
            new=new//10
        print(str(rev))

    elif (choice == 5):
        print('--------------SUM OF DIGITS------------')
        num = int(input('Enter a Number '))
        sum=0
        while(num!=0):
            sum=sum+num%10
            num=num//10
        print(str(sum))

    elif (choice == 6):
        print('--------------ARMSTRONG NO------------')
        num = int(input('Enter a Number '))
        new=num
        sum=0
        while(new!=0):
            i=new%10
            sum=sum+i*i*i
            new=new//10
        if(num==sum):
            print(str(num)+' is armstrong no')
        else:
            print(str(num)+' is not armstrong no')

    elif (choice == 7):
        print('--------------Palindrome------------')
        num = int(input('Enter a Number '))
        new = num
        rem = 0
        rev = 0
        while (new!=0):
            rem = new % 10
            rev = rev * 10 + rem
            new = new // 10
        if(rev==num):
            print(str(rev)+' is palindrome')
        else:
            print(str(num)+' is not palindrome')

    elif (choice == 8):
        print('--------------POWER------------')
        num = int(input('Enter a Number '))
        p=int(input('enter power'))
        print(str(num**p))

    elif (choice == 9):
        print('--------------FIBONACCI SERIES------------')
        num = int(input('Enter a Number '))
        f1=0
        f2=1
        f3=0
        print(str(f1))
        print(str(f2))
        for i in range(0,num):
            f3=f1+f2
            print(str(f3))
            f1=f2
            f2=f3
        print()
    elif (choice == 10):
        print('--------------POSITIVE NEGATIVE------------')
        num = int(input('Enter a Number '))
        if(num<0):
            print('Negative number')
        else:
            print('Positive number')

    else:
        print('Invalid choice.......')

    con=int(input('Do You want to continue......Press 1...'))
    if(con!=1):
        break

