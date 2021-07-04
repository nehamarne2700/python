#pattern
for i in range (1,6+1):
    for j in range(1,i):
        print('*',end=' ')
    print('\n')

#table
for i in range(1,10+1):
    for j in range(1,10+1):
        print(i*j,end='      ')
    print('\n')

#pyramid
k=10
for i in range(0,11):
    if(i%2!=0):
        print(' '*k,'*'*i)
        k=k-1;
    print()

'''
for i in range(1,level+1):
    k=0
    for j in range(1,(level+1)-i):
       print(end=' ')
    while(k != 2*i-1):
        print('*')
        k=k+1
    print('\n')
'''
#guess no
guess_no=9
guess_limit=3
guess_count=0
'''
for guess_count in range(0,guess_limit):
    num=int(input('enter guess number '))
    if(num==guess_no):
        print('correct guess after '+str(guess_count)+' attempts')
        break
    else:
        print('opps....wrong guess...try again..')
        
if(guess_count==guess_limit-1):
    print('guess limit excceded...')
'''
num=0
while(num!=guess_no and guess_count!=guess_limit):
    num=int(input('enter guess number (guess count :'+str(guess_count+1)+') :'))
    guess_count+=1
if(guess_no!=num):
    print('guess limit excceded....')
else:
    print('correct guess after ' + str(guess_count) + ' attempts')