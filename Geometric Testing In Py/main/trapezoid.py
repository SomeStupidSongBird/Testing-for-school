def getInput():
    #function that takes input from the user on the command line
    base1 = int(input("Enter the first base length of the Trapezoid: "))
    base2 = int(input("Enter the second base length of the Trapezoid: "))
    height = int(input("Enter the height of the Trapezoid: "))
    return base1,base2,height

def calcArea(base1,base2,height):
    if(base1<0 or base2<0 or height<0): #check all sides are positive
        return None
    area = (base1+base2)*height/2 #math
    return round(area,2)

def printOutput(area): #output printing
    print('----------------------------------')
    print("The Trapezoid's area: %.2f"%area)
    print('----------------------------------')

def run(): #defining a run function for better readability and exportability
    #basically a main
    b1,b2,h = getInput()
    if (b1<0 or b2<0 or h<0) : return
    area = calcArea(b1,b2,h)
    printOutput(area)

if __name__=='__main__':
    run()