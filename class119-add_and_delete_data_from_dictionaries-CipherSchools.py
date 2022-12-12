user = {
    'name': 'harsha',
    'age': 17,
    'fav_movies': ['Avengers: end game', 'pirates of caribbean', 'the pursuit of happyness'],
    'fav_tunes': ['pop'],
}

# add
user['fav_songs'] = ['the nights', 'raatan lambiyan']
print(user)

# pop
popped = user.pop('fav_tunes')
print(f"popped item is {popped}")
print(user)
popp = user.popitem()
print(user)
print(popp) #randomly removes 