a=[]
n=int(input('enter no of values you want '))
print('enter values:')
for i in range(n):
    val=int(input(str(i+1)+' NO : '))
    a.append(val)
print('List is :',a)

while(1):
    print('---------------MENU---------------')
    print('1:Maximum no\n2:Minimum no\n3:Average no')
    ch=int(input('enter your choice :'))

    if(ch==1):
        max=a[0]
        for i in range(1,n):
            if(a[i]>max):
                max=a[i]
        print('Maximum List Element Is :'+str(max))

    elif(ch==2):
        min = a[0]
        for i in range(1, n):
            if (a[i] < min):
                min = a[i]
        print('Minimum List Element Is :' + str(min))

    elif(ch==3):
        sum=0
        for i in range(n):
            sum+=a[i]
        avg=sum//n
        print('Average List Element Is :' + str(avg))

    else:
        print('Invalid choice ..')

    con=int(input('Do you want to continue....press 1...'))
    if(con!=1):
        break