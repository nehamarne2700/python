a=[]
b=[]
d=[]
nr=int(input('enter no of rows for * A * matrix you want '))
col= int(input('enter no of columns for * A * matrix you want '))
print('enter values for 1st matrix:')
for i in range(nr):
    list=[]
    for j in range(col):
        val=int(input('a['+str(i)+']['+str(j)+'] : '))
        list.append(val)
    a.append(list)

for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        print(str(a[i][j]),end=' ')
    print()

nr=int(input('enter no of rows for * B * matrix you want '))
col= int(input('enter no of columns for * B * matrix you want '))
print('enter values for 2nd matrix:')
for i in range(nr):
    list=[]
    for j in range(col):
        val=int(input('a['+str(i)+']['+str(j)+'] : '))
        list.append(val)
    b.append(list)

for i in range(0,len(b)):
    for j in range(0,len(b[i])):
        print(str(b[i][j]),end=' ')
    print()

while(1):
    print('------------------------------------------------')
    print('1:Addition\n2:Multiplication\n3:Exit')
    ch=int(input('Enter your choice : '))

    if(ch==1):
        if(len(a)==len(b)==len(a[0])==len(b[0])):
            for i in range(0,len(a)):
                ll=[]
                d.append(ll)

            for i in range(0,len(a)):
                for j in range(0,len(a)):
                    d[i].append(a[i][j]+b[i][j])
            print('Addition Is :')
            for i in range(0, len(d)):
                for j in range(0, len(d[i])):
                    print(str(d[i][j]), end=' ')
                print()
        else:
            print('Addition not possible...')

    elif (ch == 2):
        if (len(a[0]) == len(b)):
            for i in range(0, len(a)):
                ll = []
                d.append(ll)
            sum=0
            for i in range(0, len(a)):
                for j in range(0, len(b[0])):
                    for k in range(0,len(b)):
                        sum+=a[i][k]*b[k][j]
                    d[i].append(sum)
                    sum=0
            print('Multiplication Is :')
            for i in range(0, len(d)):
                for j in range(0, len(d[i])):
                    print(str(d[i][j]), end=' ')
                print()

        else:
            print('Multipliation not possible...')

    else:
       print('Inalid choice....')

    con=int((input('Do you want to continue.....press 1,..')))
    if con!=1:
        break