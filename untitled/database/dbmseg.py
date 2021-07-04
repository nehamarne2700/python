import pymysql
stud=[('neha',101),('rutuja',102),('nikita',103)]
try:
    db=pymysql.connect(user='root',password='root',host='127.0.0.1',database='mydb')
    cur=db.cursor()
    query='select database()'
    cur.execute(query)
    query="create table Student(name varchar(20),id int);"
    i=cur.execute(query)
    print(i,'Table Created..')
except Exception as e:
    print('error',e)
'''
    query="insert into Student (name,id) values(%s,%s)"
    i=cur.execute(query,('neha',101))
    if(i>0):
        print('Record inserted ...')
    db.commit()
    query = 'select * from Student'
    cur.execute(query)
    print('Student table contents after insert: ')
    print(cur.fetchall())
'''

'''
    query="update Student set name='Akanksha' where name='nikita'"
    i = cur.execute(query)
    if (i > 0):
        print('Record updated ...')
    db.commit()
    query = 'select * from Student'
    cur.execute(query)
    print('Student table contents after update: ')
    print(cur.fetchall())
    query="delete from Student where name='Akanksha'"
    i = cur.execute(query)
    if (i > 0):
        print('Record deleted ...')
    db.commit()
    query = 'select * from Student'
    i=cur.execute(query)
    print(i,' Student table contents after delete: ')
    print(cur.fetchall())
except Exception as e:
    print('error',e)
    db.rollback()
finally:
    db.close()
'''