def greatest(a,b,c):
    if a>b and a>c:
        print(f"{a} is greatest")
    elif b>a and b>c:
        print(f"{b} is greatest")
    else:
        print(f"{c} is  greatest")
n1 = int(input("enter a number: "))
n2 = int(input("enter a number: "))
n3 = int(input("enter a number: "))
print(greatest(n1,n2,n3))