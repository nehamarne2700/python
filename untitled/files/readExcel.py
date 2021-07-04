import pandas as pd

df=pd.read_excel('Book1.xlsx',)
print(df)
df.insert(loc=8,column0-='pid',value='90')
#df.update({'srno':[int(9)],'pid':[int(109)],'pname':['plant'],'pprice':[int(99)],'qty':[int(5)]},overwrite=False)
print(df)







'''
file='Book1.xlsx'
newfile=pd.read_excel(file)
print('Excel file data : ')
print(newfile)
print('total rows and columns in file : ',newfile.shape)
print('data sort based on price : ')
newfile=newfile.sort_values(['pprice'],ascending=False)
print(newfile)
print('new file after update : ')
newfile['total']=newfile['pprice']*newfile['qty']
newfile.to_excel('Book1.xlsx',index=False)
'''
'''
df=pd.DataFrame([['a','b'],['1','2']],columns=['name','no'])
df.to_excel('opex.xlsx')
'''