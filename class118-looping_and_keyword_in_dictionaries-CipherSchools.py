user = {
    'name' : 'harsha',
    'age' : 17,
    'fav_movies' : ['Avengers: end game','pirates of caribbean','the pursuit of happyness'],
    'fav_tunes' : ['pop'],

}
if 'name' in user:
    print('present')
else:
    print('not present')

if 'harsha' in user.values():
    print('present')
else:
    print('not present')

# loops in dictionary

for i in user.values():
    print(i)
for i in user:
    print(i)
for i in user:
    print(user[i])
user_values = user.values()
print(user_values)
print(type(user_values))
user_keys = user.keys()
print(user_keys)
print(type(user_keys))
# these are not lists you can't add delete data from dict values like list but you can iterate through dict values
user_items = user.items()
print(user_items)
print(type(user_items))

for key, value in user.items():
    print(f"key is {key} and value is {value}")
