# def is_palindrome(a):
#     if a == a[::-1]:
#         return True
#     return False
def is_palindrome(a):
    return a == a[::-1]
a = input("enter a word: ")
print(is_palindrome(a))