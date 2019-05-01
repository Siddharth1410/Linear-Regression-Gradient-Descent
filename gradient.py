#Siddharth Vadgama
#UTA ID-1001397508	
import numpy as np
import matplotlib.pyplot as plt
def cost(cities,hospital):
        sum=0
        for i in range(0,len(cities)):
                sum+=(cities[i][0]-hospital[0])*(cities[i][0]-hospital[0])+(cities[i][1]-hospital[1])*(cities[i][1]-hospital[1])
        return sum
def cost_x(cities,hospital):
	sum=0
	for i in range(0,len(cities)):
		sum+=2*(-1*cities[i][0]+hospital[0])
	return sum
	
def cost_y(cities,hospital):
	sum=0
	for i in range(0,len(cities)):
		sum+=2*(-1*cities[i][1]+hospital[1])
	return sum

def positionHospital(c, h, alpha, tol) :
    i=0
    res = np.array([[]])
    res=np.append(res,h)
    while True:
    	
        h1=h[0]-alpha*cost_x(c,h)
        h2=h[1]-alpha*cost_y(c,h)
        temp=np.array([h1,h2])
        temp2=np.array([temp])
        res=np.append(res,temp2)
        print('k=',i,'\tcost=',cost(c,h),'\tgrad=[',cost_x(c,h),',',cost_y(c,h),']','\thospital',temp)
        if (np.linalg.norm((temp-h),2)<tol):
    	    break
        h=temp
    	
        i=i+1
    res=np.reshape(res,(int(len(res)/2),2))
    return res	

def plotCoor(cities, hospital):
    #print(hospital)
    #print(np.shape(hospital))
    plt.plot(cities[:,0],cities[:,1],'ob')
    plt.plot(hospital[:,0],hospital[:,1],'xr')
    plt.title('Cities and Hospital')
    plt.show()


###################  main  ###################
if __name__ == "__main__":
    #  coordinates of cities
    cities = np.array([[ 0,   0],
                       [30, 110],
                       [60, 100],
                       [50,  50]])
    
    #   initial coordinates of hospital
    hosp = np.array([0, 55])
    alpha = 0.01
    tol = 1
    
    hNew = positionHospital(cities, hosp, alpha, tol) 
    plotCoor(cities, hNew)
    
