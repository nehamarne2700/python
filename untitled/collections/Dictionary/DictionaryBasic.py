employee={
    "name":"neha",
    "address":"Pune",
    "no":205240
}

print('Dictionary : ',employee)
print('Dictionary items : ',employee.items())
print('Dictionary keys : ',employee.keys())
print('Dictionary values : ',employee.values())

print('Dictionary name :',employee.get("name"))

employee["name"]="akanksha"

print('New Dictionary name : ',employee.get("name"))
keys=list(employee.keys())
print(keys[1])
