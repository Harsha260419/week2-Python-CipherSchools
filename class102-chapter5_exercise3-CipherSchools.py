def ultaa(l):
    num = []
    for i in range(len(l)):
        a = l[i][::-1]
        num.append(a)
    return num
any = ['abc', 'def']
print(ultaa(any))

def ulta(l):
    thing = []
    for i in l:
        thing.append(i[::-1])
    return thing
word = ['abc','madam']
print(ulta(word))
