#Makeda joseph
#04/24/2017



def calculater_tax(income):
    if income < 250000:
        tax = income *.40
    else:
        tax = 250000*.40 + (income - 250000) *.8

    return tax

def main():
    
    y = calculater_tax(300000)
    print (y)

main()
