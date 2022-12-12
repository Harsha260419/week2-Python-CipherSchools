def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("you cannot divide a number by zero")
    except TypeError as err:
        print(err)
    except:
        print("unexpected error")
print(divide(10,'2'))
