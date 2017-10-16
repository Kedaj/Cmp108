#Makeda Joseph
#03/08/2017



name = input('Please enter you list of names:')
namelist= name.split(";")

print("You entered:\n")

for n in namelist:
    W = n.split(",")
    print(W[1], W[0])


print("Thank you for using my name organizer")
        
