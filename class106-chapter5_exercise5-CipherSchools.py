def com(l, m):
    emp = []
    for i in range(0,len(l)):
        if l[i] in m:
            emp.append(l[i])
    return emp
ll = list(range(1,21))
mm = list(range(1,11))
print(com(ll,mm))

def com(l, m):
    emp = []
    for i in l:
        if i in m:
            emp.append(i)
    return emp
ll = list(range(1,21))
mm = list(range(1,11))
print(com(ll,mm))

