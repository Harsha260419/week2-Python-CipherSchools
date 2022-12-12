def name(naam):
    print(naam[-1])
naam = input("name: ")
name(naam)

def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"
print(odd_even(9))
# same as above one
def odd_even(num):
    if num%2 == 0:
        return "even"
    return 'odd'
print(odd_even(9))

def is_even(num):
    if num%2 == 0:
        return True
    return False
print(is_even(7))

def is_even(num):
    return num%2 == 0
print(is_even(7))
