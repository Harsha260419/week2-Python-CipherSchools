user = {
    'name' : 'harsha',
    'age' : 17,
    'fav_movies' : ['Avengers: end game','pirates of caribbean','the pursuit of happyness'],
    'fav_tunes' : ['pop'],
}
additional = {
    'name' : 'Harsha Sai', #updates the info if it is present in the original one
    'state' : 'telangana',
    'hobbies' : ['coding', 'reading books', 'web series']


}
user.update(additional)
print(user)
user.update({}) #means nothing added and this will not delete existig data
print(user)
