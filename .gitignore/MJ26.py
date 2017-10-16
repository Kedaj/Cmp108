#Makeda Joseph
#03/13/2017




nums = input("Please enter your list of number:")
numsList = nums.split(" ")
total = 0

for n in numsList:
    numsList2 = int(n)
    print(n)
    total = (total + numsList2)
 

print("Your total is," + str(total))
