# dictionaries intro
# why we use dictionaries?
# because of limitations of lists, lists are not enough to represent real data
# dictionaries are unordered collections of data key : value pair

user = {'name': 'Harsha', 'age':17}
print(user)
print(type(user))
user1 = dict(name = 'harsha', age = 17)
print(user1)
print(user['name']) #accessing the data from dictionaries
# there is no indexing in dictionaries
# you can store lists, strings, numbers, dictionaries inside dictionaries

user_info = {}
user_info['name'] = 'elon'
print(user_info['name'])
