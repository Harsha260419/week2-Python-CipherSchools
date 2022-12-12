# d = {'name' : 'unknown', 'age' : 'unknown'}
d = dict.fromkeys(('name',  'age', 'height'), 'unknown')
d = dict.fromkeys("abc", 'unknown')
d = dict.fromkeys(range(1,11), 'unknown')
d = dict.fromkeys(['name','age'], ['unknown','unknown'])
print(d)

# get method for accessing keys
d = {'name' : 'unknown', 'age' : 'unknown'}
# print(d['names'])
print(d.get('names')) #better for accessing the keys

if d.get('names'):
    print('present')
else:
    print('not present')
    # if None ---> False, else ---> True

# clear method
# d.clear()
# print(d)

# copy method
d1 = d.copy()
print(d1)
# if you pop something from d1 then d will remain unchanged it doesn't get affected