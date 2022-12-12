name = input("enter your name: ")
tem = ""
for i in range(0,len(name)):
    if name[i] not in tem:
        print(f"{name[i]}: {name.count(name[i])}")
        tem += name[i]
        