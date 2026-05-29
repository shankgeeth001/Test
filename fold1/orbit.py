import matplotlib
import numpy as np

class M1: 

    m1 = 2 
    coord1 = np.array([0, 2]) 
    
    def __init__(self,a1):
        self.a1 = 0
 

class M2: 

    m2 = 3 
    coord2 = np.array([6,2]) 
    a2 = 0


G = 3
R = ((M2.coord2[0] - M1.coord1[0])**2 + (M2.coord2[1] - M1.coord1[1])**2)**(1/2)

F = (G*M1().m1*M2().m2)/R**2 

M1().a1 = F/M1().m1
M2().a2 = F/M2().m2

print(M1().a1)
print(M2().a2)