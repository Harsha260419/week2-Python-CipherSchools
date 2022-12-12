user = {
    'name' : 'harsha',
    'age' : 17,
    'age' : 18 #overrides the previous value
}
print(user.get('names', 'not found!')) #bypassing None and printing the message what we want
print(user)
