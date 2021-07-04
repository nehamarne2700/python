from covid import Covid

import matplotlib.pyplot as plt

covid=Covid()
cnames=[]
name=input("Enter The Country Name : ")

virusdata=covid.get_status_by_country_name(name)
all=covid.list_countries()


for l in range(len(all)):
    cnames.append(all[l]['name'])

print(cnames)

remove=['id','country','latitude','longitude','last_update']

for i in remove:
    virusdata.pop(i)

tot=virusdata.pop('confirmed')

id=list(virusdata.keys())
values=[str(i) for i in virusdata.values()]

a=plt.pie(values,labels=id,colors=['r','y','g','b'],autopct='%1.1f%%')
a.title("COUNTRY : "+name.upper()+"\nTOTAL CASES : "+str(tot))
a.legend()
a.show()
a.savefig("output.png")