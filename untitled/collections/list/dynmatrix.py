a=[]
b=[]
d=[]
nr=int(input('enter no of rows for * A * matrix you want '))
print('enter values for 1st matrix:')
for i in range(nr):
    list=[]
    col= int(input('enter no of columns for '+str(i)+' th row :'))
    for j in range(col):
        val=int(input('a['+str(i)+']['+str(j)+'] : '))
        list.append(val)
    a.append(list)

for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        print(str(a[i][j]),end=' ')
    print()

nr=int(input('enter no of rows for * B * matrix you want '))
print('enter values for 2nd matrix:')
for i in range(nr):
    list=[]
    col= int(input('enter no of columns for '+str(i)+' th row :'))
    for j in range(col):
        val=int(input('a['+str(i)+']['+str(j)+'] : '))
        list.append(val)
    b.append(list)

for i in range(0,len(b)):
    for j in range(0,len(b[i])):
        print(str(b[i][j]),end=' ')
    print()
