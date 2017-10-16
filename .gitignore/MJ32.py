#Makeda Joseph
#03/22/2017


def getGrades():
    n = input("enter file")
    infile = open (n,"r")
    contents = infile.read()

    infile.close()

    return contents

def calculateAverage(g):
    words = g.split(",")
    total = 0
    for w in words:
        total = total + int(w)
        avg = total/len(w)

        return avg

def main():
    grades = getGrades()
    avg = calculateAverage(grades)
    print("The calculated average is:",avg)

main()
    
    
    
