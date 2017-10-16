#Makeda Joseph
#03/15/2017


name = input("Please enter your file name:")

total = 0

infile = open(name)

for n in infile:
    total = total + float(n)

print("The sum of your numbers is", total)
    
    
            
    
