def greater(a,b):
    if a>b:
        return a
    return b
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c 



def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger, c)
print(new_greatest(10,20,40))


# The new_greatest() function uses the greater() function to find the largest of the three numbers. First, it compares a and b and returns the greater of the two. Then, it compares the result with c and returns the greater of the two.

# Here is how the new_greatest() function would work for the input 10, 20, 40:

# The new_greatest() function is called with the arguments 10, 20, and 40.
# The greater() function is called with the arguments 10 and 20. This returns 20.
# The greater() function is called with the arguments 20 and 40. This returns 40.
# The new_greatest() function returns the value 40.
# Therefore, the call to new_greatest(10, 20, 40) should return 40.

# kiss - keep it simple stupid