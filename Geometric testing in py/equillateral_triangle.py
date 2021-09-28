#find area
def getInput():
    side = int(input("Enter the length of a side of the Triangle: "))
    return  side

def calcArea(side1,side2):
    area = math.sqrt(side1**2+(side2/2)**2) * side2
    return area

def printOutput(area):
    print('----------------------------------')
    print("The Triangle's area: %.2f"%area)
    print('----------------------------------')

def run(): #defining a run function for better readability and exportability
    s = getInput()
    if (s<0) : return
    area = calcArea(s,s)
    printOutput(area)

if __name__=='__main__':
    run()