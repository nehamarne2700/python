#tupple is unhangable ordered collection
tup=(10,20,30,40,'AB')
print('tupple 1: ',tup)

print('tupple 1 type',type(tup))

#dec
tup1=tuple((1,2,3,4))

#can declare tupple as follow also using constructor

print('tupple 2 : ',tup1)
print('tupple 2 type',type(tup))

#can access elements by index
for i in range(len(tup)):
    print('tup['+str(i)+'] '+str(type(tup[i]))+' : '+str(tup[i]))

print('\ntup1[3] : ',tup1[3])

#cannot change random element form tupple
#tup[2]=50
#TypeError: 'tuple' object does not support item assignment

#can delete whole tupple
del tup
#print(tup)   (error)

tup=(1,2,3,4)
tup1=(5,6,7,8)
tup2=(tup+tup1)
print('tup: ',tup)
print('tup1 : ',tup1)
print('merge tup & tup1 in tup2 :',tup2)

print('tupple within tupple')
tup2=(tup,tup1)
print('tup2 :',tup2)
print('tup2[0] :',tup2[0])
print('tup2[1] :',tup2[1])

print('\nlist within tupple ')
list1=[12,13,14,15]
list2=[21,22,23,24]
tup=(list1,list2)

print('tup : ',tup)

list1[3]='new'

print('new tuple :',tup)
