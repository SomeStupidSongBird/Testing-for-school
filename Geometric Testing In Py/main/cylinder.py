#find volume and surface area
import math
 
def getInput(): #usual cl input
    print("----------------------------------")
    radius = int(input("Enter the radius of the Cylindar: "))
    height = int(input("Enter the height of the Cylindar: "))
    if(radius<0 or height<0):
        print("All values must be positive")
    print("----------------------------------")
    return radius, height

def calcVolume(radius,height):
    if(radius<0 or height<0): #positive check
        return None
    volume = math.pi*(radius**2)*height #math
    return volume

def calcSurfArea(radius,height):
    if(radius<0 or height<0): #vibe check
        return None
    surfaceArea = math.pi*2*radius*(radius+height) #math
    return surfaceArea

def calcLatSurfArea(radius,height):
    if(radius<0 or height<0): #vibe check
        return None
    latSA = 2*math.pi*radius*height
    return latSA

def calcEndSurfArea(radius):
    if(radius<0):
        return None
    area = math.pi*radius*radius
    return area

def printOutput(volume,surfaceArea,lateralSurfaceArea,endSurfaceArea):  #cl output
    print('----------------------------------')
    print("The Cylindar's volume: %.2f"%volume)
    print("The Cylindar's surface area: %.2f"%surfaceArea)
    print("The Cylindar's lateral surface area: %.2f"%lateralSurfaceArea)
    print("The Cylindar's end surface area: %.2f"%endSurfaceArea)
    print('----------------------------------')

def run(): #defining a run function for better readability and exportability
    r,h = getInput()
    if (r<0 or h<0) : return
    volume = calcVolume(r,h)
    sA = calcSurfArea(r,h)
    latsa = calcLatSurfArea(r,h)
    endsa = calcEndSurfArea(r)
    printOutput(volume,sA,latsa,endsa)

if __name__=='__main__':
    run()