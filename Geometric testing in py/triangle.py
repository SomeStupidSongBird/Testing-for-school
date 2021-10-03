import math

#find area
def getInput():
    side1 = int(input("Enter the first side of the Triangle: "))
    side2 = int(input("Enter the second side of the Triangle: "))
    side3 = int(input("Enter the third side of the Triangle: "))
    return side1,side2,side3

def calcArea(side1,side2,side3):
    if(side1<0 or side2<0 or side3<0):
        return None
    if(side1+side2<=side3 or side1+side3<=side2 or side2+side3<=side1):
        return None
    Alpha = math.acos((side2**2+side3**2-side1**2)/2*side2*side3)
    area = .5*side1*(side3*math.sin(Alpha))
    return area

def printOutput(area):
    print('----------------------------------')
    print("The Triangle's area: %.2f"%area)
    print('----------------------------------')

def run(): #defining a run function for better readability and exportability
    s1,s2,s3 = getInput()
    if (s1<0 or s2<0 or s3<0) : return
    if(s1+s2<s3 or s1+s3<s2 or s2+s3<s1) : return
    area = calcArea(s1,s2)
    printOutput(area)

if __name__=='__main__':
    run()