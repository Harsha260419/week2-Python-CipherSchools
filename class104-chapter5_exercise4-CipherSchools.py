def filteri(l):
    div = []
    divi = []
    dev = []
    for i in l:
        if i%2 == 0:
            divi.append(i)
        else:
            div.append(i)
    dev.append(div)
    dev.append(divi)
    return dev
num = list(range(1,11))
print(filteri(num))

def filter_o_e(l):
    oddd = []
    evenn = []
    for i in l:
        if i%2 == 0:
            evenn.append(i)
        else:
            oddd.append(i)
    final = [oddd, evenn]
    return final 
print(filter_o_e(num))
