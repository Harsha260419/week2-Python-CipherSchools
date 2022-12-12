x = 5 #global variable

def func():
    global x
    x = 7 #local variable
    return x
print(x)
print(func())
# if you print the x value before calling the function then it's value is not be printed as 7 because we did that before calling that function but if you print that after calling the function it'll be 7