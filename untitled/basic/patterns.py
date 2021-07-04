#pattern
for i in range (1,6+1):
    for j in range(1,i):
        print('*',end=' ')
    print('\n')

k=10
for i in range(0,11):
    if(i%2!=0):
        print(' '*k,'*'*i)
        k=k-1;
    print()

k=5
for i in range(0,6):
    print(' '*k,' *'*i)
    k=k-1;
    print()

print()
for i in range (6,0,-1):
    for j in range(i,0,-1):
        print('*',end=' ')
    print('\n')

for i in range(1,6+1):
    for j in range(0,i):
        print(str(i),end=' ')
    print('\n')

for i in range(1,6+1):
    for j in range(0,i):
        print(str(j+1),end=' ')
    print('\n')

k=1
for i in range(1,6+1):
    for j in range(0,i):
        print(str(k),end=' ')
        k+=1
    print('\n')

a=65
for i in range(1,6+1):
    for j in range(0,i):
        print(chr(a),end=' ')
        a+=1
    print('\n')

a=97
for i in range(1,6+1):
    for j in range(0,i):
        print(chr(a),end=' ')
        a+=1
    print('\n')

k=5
for i in range(0,6):
    print(' '*k,' *'*i)
    k=k-1;
k=0
for i in range(5,-1,-1):
    print(' '*k,' *'*i)
    k=k+1;