'''
csv->comma seperated file
101,neha
102,rutuja
103,nikita
104,akanksha
'''
import csv

with open('myfile.csv','r')as file:
    reader=csv.reader(file)

    for row in reader:
        print(row)
        for i in row:
            print("data : ",i)
        print('\n')


with open('mycsv1.csv', 'w', newline='')as file:
    writer=csv.writer(file)
    writer.writerow(['Rollno','name'])
    writer.writerow(['101','neha'])
    writer.writerow(['102','rutuja'])
    writer.writerow(['103','akanksha'])
