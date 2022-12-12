mixed = (1,2,3,4.0)

# loops in tuple
for i in mixed:
    print(i)

a = 0
while a in range(0,len(mixed)):
    print(mixed[a])
    a += 1

# tuple with one element
num = (1) #this is not tuple the type outcome will be int to make this into tuple we should write , after the first element if we want only one element in tuple
print(type(num))
numm = (1,)
print(type(numm))

# tuple without parenthesis
guitars = 'yamaha', 'baton rouge', 'taylor'
print(type(guitars))

# tuple unpacking
guitarists = ('maneli jamal', 'justin bieber', 'shawn mendes')
g1, g2, g3 = (guitarists)
print(g1)

# list inside tuples
favs = ('elon musk', ['ratan tata', 'professor', 'eleven', 'sergio', 'tokyo'])
favs[1].pop()
favs[1].append('tokyo')
print(favs)

# functions which can be used with a tuple
# min, max, sum
print(sum(mixed))