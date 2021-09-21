import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def scatterLine(x,y,m,c,name): #this will graph entered data with x,y being the scatter plot data and m,c being the line data
    rang = np.linspace(x.min(),x.max()) #build the view range of the data
    line = m*rang+c #this is the line equation
    plt.plot(x,y,'bo',label=name) #polt the scatter graph 
    plt.plot(rang,line,'-r',linestyle = 'dashed') #plot the line graph
    names = name.split(' ')

    plt.xlabel(names[0])
    plt.ylabel(names[2])
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

def calcSlopeIntPearR(x,y): #x and y are array-like (not checked, please be careful)
    #define general statistics
    n = len(x)
    xavg = np.sum(x)/n
    yavg = np.sum(y)/n

    #define new arrays to use in equation
    xp = x-xavg
    yp = y-yavg
    xyp = xp*yp
    xpsqr = xp*xp

    slope = np.sum(xyp)/np.sum(xpsqr)
    intercept = yavg-slope*xavg
    
    #define new arrays to use in equation
    xy = x*y
    xsqr = x*x
    ysqr = y*y
    r = (n*np.sum(xy)-(np.sum(x)*np.sum(y)))/(np.sqrt(n*np.sum(xsqr)-np.sum(x)**2)*np.sqrt(n*np.sum(ysqr)-np.sum(y)**2))
    #print("Slope: "+str(slope))
    #print("Intercept: "+str(intercept))
    #print("r^2: "+str(r**2))
    return slope, intercept, r

def getInput(path,col1,col2):
    ind = pd.read_excel(path)
    x = ind[col1]
    y= ind[col2]
    return x,y

def main():
    path = "C:/Users/ferchrj/Desktop/working with py/lab_3/BodyFat.xls"
    sectname = "Bodyfat and Density"
    print(sectname)
    x,y = getInput(path,'BODYFAT','DENSITY')
    m,c,r = calcSlopeIntPearR(x,y)

    scatterLine(x,y,m,c,sectname)
    est = m*7+c
    print("Bodyfat = 7, estimated Density = "+str(est))

    sectname = "Height and Weight"
    print(sectname)
    x,y = getInput(path,'HEIGHT','WEIGHT')
    m,c,r = calcSlopeIntPearR(x,y)
    
    scatterLine(x,y,m,c,sectname)

if __name__=='__main__':
    main()
