#find volume and surface area
import math

def getInput():
    # function that takes input from the user
    print("----------------------------------")
    radius = int(input("Enter the radius of the Cone: "))
    height = int(input("Enter the height of the Cone: "))
    if(radius<0 or height<0):
        print("All values must be positive")
    print("----------------------------------")
    return radius, height

def calcVolume(radius,height):
    if(radius<0 or height<0): #check if it's positive again
        return None
    volume = math.pi*(radius**2)*height/3  #math
    return round(volume,2)

def calcSurfArea(radius,height):
    if(radius<0 or height<0): #check if it's positive again
        return None
    surfaceArea = math.pi*(math.sqrt(radius**2+height**2)+radius)*radius  # math
    return round(surfaceArea,2)

def calcLatteralSurfArea(radius,height):
    if(radius<0 or height<0): #check if it's positive again
        return None
    latSA = math.sqrt(radius**2+height**2)*math.pi*radius
    return round(latSA,2)

def printOutput(volume,surfaceArea,lateralSurfaceArea): #just formatted printing
    print('----------------------------------')
    print("The Cone's volume: %.2f"%volume)
    print("The Cone's surface area: %.2f"%surfaceArea)
    print("The Cone's lateral surface area: %.2f"%lateralSurfaceArea)
    print('----------------------------------')

def run(): #defining a run function for better readability and exportability
    # this is basically the main function
    r,h = getInput()
    if (r<0 or h<0) : return
    volume = calcVolume(r,h)
    sA = calcSurfArea(r,h)
    latSA = calcLatteralSurfArea(r,h)
    printOutput(volume,sA,latSA)

if __name__=='__main__':
    run()