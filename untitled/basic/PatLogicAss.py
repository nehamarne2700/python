def pyramid():
    k = 5
    for i in range(0, 6):
        print(' ' * k, ' *' * i)
        k = k - 1;
        print()

def pascal():
    k = 10
    for i in range(0, 11):
        if (i % 2 != 0):
            print(' ' * k, '*' * i)
            k = k - 1;
        print()

def diamond():
    k = 5
    for i in range(0, 6):
        print(' ' * k, ' *' * i)
        k = k - 1;
    k = 0
    for i in range(5, -1, -1):
        print(' ' * k, ' *' * i)
        k = k + 1;

def alphaPat():
    a = 65
    for i in range(1, 6 + 1):
        for j in range(0, i):
            print(chr(a), end=' ')
            a += 1
        print('\n')

    a = 97
    for i in range(1, 6 + 1):
        for j in range(0, i):
            print(chr(a), end=' ')
            a += 1
        print('\n')

def numPat():
    for i in range(1, 6 + 1):
        for j in range(0, i):
            print(str(i), end=' ')
        print('\n')

    for i in range(1, 6 + 1):
        for j in range(0, i):
            print(str(j + 1), end=' ')
        print('\n')

    k = 1
    for i in range(1, 6 + 1):
        for j in range(0, i):
            print(str(k), end=' ')
            k += 1
        print('\n')


def factor():
    print('--------------FACTOR--------------')
    num = int(input('Enter a Number '))
    print('Factor of ' + str(num) + ' are :')
    for i in range(1, (num // 2) + 1):
        if (num % i == 0):
            print('', i)

def factorial():
    print('--------------FACTORIAL------------')
    num = int(input('Enter a Number '))
    f = 1
    for i in range(1, num + 1):
        f = f * i
    print('Factorial of ' + str(num) + ' is ' + str(f))

def prime():
    print('--------------PRIME------------')
    num = int(input('Enter a Number '))
    flag = 1
    for i in range(2, (num // 2) + 1):
        if (num % i == 0):
            flag = 0
            break
    if (flag == 1):
        print(str(num) + ' is Prime no')
    else:
        print(str(num) + ' is not a Prime no')

def reverse():
    print('--------------Reverse------------')
    num = int(input('Enter a Number '))
    new = num
    rem = 0
    rev = 0
    while (new != 0):
        rem = new % 10
        rev = rev * 10 + rem
        new = new // 10
    print(str(rev))

def sumOfDigits():
    print('--------------SUM OF DIGITS------------')
    num = int(input('Enter a Number '))
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    print(str(sum))

def armstrong():
    print('--------------ARMSTRONG NO------------')
    num = int(input('Enter a Number '))
    new = num
    sum = 0
    while (new != 0):
        i = new % 10
        sum = sum + i * i * i
        new = new // 10
    if (num == sum):
        print(str(num) + ' is armstrong no')
    else:
        print(str(num) + ' is not armstrong no')

def palindrome():
    print('--------------Palindrome------------')
    num = int(input('Enter a Number '))
    new = num
    rem = 0
    rev = 0
    while (new != 0):
        rem = new % 10
        rev = rev * 10 + rem
        new = new // 10
    if (rev == num):
        print(str(rev) + ' is palindrome')
    else:
        print(str(num) + ' is not palindrome')

def power():
    print('--------------POWER------------')
    num = int(input('Enter a Number '))
    p = int(input('enter power'))
    print(str(num ** p))

def fibonacci():
    print('--------------FIBONACCI SERIES------------')
    num = int(input('Enter a Number '))
    f1 = 0
    f2 = 1
    f3 = 0
    print(str(f1))
    print(str(f2))
    for i in range(0, num):
        f3 = f1 + f2
        print(str(f3))
        f1 = f2
        f2 = f3
    print()

def posneg():
    print('--------------POSITIVE NEGATIVE------------')
    num = int(input('Enter a Number '))
    if (num < 0):
        print('Negative number')
    else:
        print('Positive number')

while(1):
    print('------------------------MAIN MENU-----------------------')
    print('\n1:Patterns\n2:Logic\n3:EXIT')
    choice=int(input('enter your choice'))

    if(choice==1):
        while(1):
            print('-------------------PATTERN MENU------------------')
            print('1:Pyrmid\n2:Pascal triangle\n3:Diamond\n4:Alphabet pattern\n5:Numerical Pattern\n6:EXIT')
            ch1=int(input('enter your choice'))
            if (ch1 == 1):
                pyramid()

            elif (ch1 == 2):
                pascal()

            elif (ch1 == 3):
                diamond()

            elif (ch1 == 4):
                alphaPat()

            elif (ch1 == 5):
                numPat()

            elif (ch1 == 6):
                break
            else:
                print('Invalid choice')

            con1 = int(input('Do You want to continue [PATTERNS]......Press 1...'))
            if (con1 != 1):
                break

    elif(choice==2):
        while(1):
            print('------------------LOGIC MENU-------------------')
            print('\n1:Factor\n2:Factorial\n3:Prime No\n4:Reverse No\n5:Sum of digits')
            print('6:Armstrong no\n7:Palindrome No\n8:Power\n9:Fibbonacci Series\n10:Postive/Negative\n11:EXIT')
            ch2=int(input('enter your choice'))

            if(ch2==1):
                factor()

            elif(ch2==2):
                factorial()

            elif (ch2 == 3):
                prime()

            elif (ch2 == 4):
                reverse()

            elif (ch2 == 5):
                sumOfDigits()

            elif (ch2 == 6):
                armstrong()

            elif (ch2 == 7):
                palindrome()

            elif (ch2 == 8):
                power()

            elif (ch2 == 9):
                fibonacci()

            elif (ch2 == 10):
                posneg()

            elif(ch2==11):
                break

            else:
                print('Invalid choice.......')

            con2=int(input('Do You want to continue [LOGIC]......Press 1...'))
            if(con2!=1):
                break
    elif(choice==3):
        break

    else:
        print('Inavlid choice')

    con = int(input('Do You want to continue [MAIN MENU]......Press 1...'))
    if (con != 1):
        break