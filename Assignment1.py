# -*- coding: utf-8 -*-
"""

@author: Joep

"""


from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np


sigma= 2
kappa=0.3
beta=0.99
phi_1=1.5
phi_2=0.2

#1

N=1000 #simualte N periods    

Y=np.zeros(N)
Pi=np.zeros(N)
ni=np.zeros(N)#nominal interest rate
EY=np.zeros(N)
EPi=np.zeros(N)


#intital values

Y[0] =0.1
Pi[0]=-0.2       


for i in range(1,N):

    EY[i]=Y[i-1]
    EPi[i]=Pi[i-1]
        
    ni[i]=phi_1*EPi[i]+phi_2*EY[i]
    Y[i]=EY[i]-1/sigma*(ni[i]-EPi[i])   
    Pi[i]=beta*EPi[i]+kappa*Y[i]
        
        
    #2

















plt.figure()    
plt.subplot(2, 2, 1)
plt.plot([Y[i]*100 for i in range(N)],linewidth=2)
plt.title('Output gap')
plt.ylabel('X_t')
plt.xlabel('t')


  
plt.subplot(2, 2, 2)
plt.plot([Pi[i]*100 for i in range(N)],linewidth=2)
plt.title('Inflation')
plt.ylabel('Pi_t')
plt.xlabel('t')


   
plt.subplot(2, 2, 3)
plt.plot([ni[i]*100 for i in range(N)],linewidth=2)
plt.title('Nominal Interest Rate')
plt.ylabel('i_t')
plt.xlabel('t')
plt.tight_layout() #



print('Final Output gap is', Y[N-1])             
print('Final Inflation is', Pi[N-1])






#4










A=np.array([[1,0,1/sigma],
            [-kappa,1,0],
            [0,0,1]])
            
Ainv=np.linalg.inv(A)

#5
def Model(coef):
    B=np.zeros(len(coef))
    expY=coef[0]
    expPi=coef[1]

    
    B[0]=expY+1/sigma*expPi
    B[1]=beta*expPi
    B[2]=phi_1*expPi+phi_2*expY
    
    z=np.dot(Ainv,B)

    return z






# 6
print('when we use input',[Y[N-1],Pi[N-1],ni[N-1]], 'then output is',   Model([Y[N-1],Pi[N-1],ni[N-1]]))


#7    









def Model_dif(coef):
    B=np.zeros(len(coef))
    expY=coef[0]
    expPi=coef[1]

    
    B[0]=expY+1/sigma*expPi
    B[1]=beta*expPi
    B[2]=phi_1*expPi+phi_2*expY
    
    z=np.dot(Ainv,B)
    dif=z-np.array(coef)

    return dif












#8
init = [1,1,1]
 
[msv_coefficients,inf,ier,mes] = fsolve(Model_dif, init,full_output=1)  
if ier != 1:
    print (mes)

#9
print('The constants in the msv solution are', msv_coefficients)




    
 
