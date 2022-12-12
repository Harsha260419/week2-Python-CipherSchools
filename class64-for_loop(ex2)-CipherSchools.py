# take the input from the user and ass up all the digits given in the input
# take the input
# start a for loop which is iterating from 0 to int(len(num))
# i would also create a variable which is empty then i will add up everything which i iterate over total += i
# i print the total variable




total = 0
num = input("enter a number: ")
for i in range(0,len(num)):
    total += int(num[i])
print(total)
