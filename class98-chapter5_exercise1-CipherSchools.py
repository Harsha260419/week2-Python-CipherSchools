numbers = list(range(1,11))
def square(l):
    two = []
    for i in l:
        two.append(i**2)
    return two
print(square(numbers))