info = {'name' : 'Inam', 'age':23, 'eligible': True}

print(info)

info.update({'age': 30})
info.update({'DOB': 1994})

print(info)

info.pop('name')
print(info)

info.popitem()
print(info)

del info['age']
print(info)

info.clear()
#or del info
print(info)