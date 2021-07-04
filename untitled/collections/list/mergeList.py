list1=[10,20,30]
list2=[40,50,60,70,80]

list3=[list1,list2]

print('list1 : ',list1)
print('list2 : ',list2)
print('list3 : ',list3)

for i in range(len(list3)):
    if(i==0):
        n=len(list1)
    else:
        n=len(list2)
    for j in range(n):
        print(list3[i][j])