numbers = list(range(1,11))
def rev(l):
    reve = []
    for i in range(len(l)):
        a = l.pop()
        reve.append(a)
    return reve
print(rev(numbers))

