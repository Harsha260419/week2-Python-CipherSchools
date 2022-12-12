numbers = list(range(1,11))
print(numbers)
numbers.pop()
print(numbers.pop())
print(numbers)
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 55, 65, 1]
print(number.index(1))
print(number.index(1, 1, 11)) # first one is the number we want to find out and second is the index from we want to start and third one is to index where we want to end 
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))