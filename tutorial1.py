# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# Exercises
    
# set up list x
x = [1,8,3,4,7,6,2,5]
    
#a)

# initialize a list with zeros with the same length as x


y=[0]*len(x)


i=0
for x_element in x:
    if x_element<5:
        y[i]=1
    i+=1
    
    
# unpythonic loop with explicit indices (yet useful)    
for i in range(8):
    if x[i]<5:
        y[i]=1

#pythonic loop
y=[]
for x_element in x:
    if x_element<5:
        y.append(1)
    else: 
        y.append(0)
  
print(y)         
#b)


z=[]
for x_element in x:
    if x_element<5:
        z.append(x_element)
print(z)    
    
    
#c)
w=[]
for x_element in x:
    if x_element<3:
        w.append(x_element)
    elif x_element>5:
        w.append(x_element)

print(w)  
        
w=[]
for x_element in x:
    if (x_element<3) or (x_element>5):
        w.append(x_element)      
print(w)  
       
#d) 

for j in range(len(w)-1):
    for k in range(len(w)-1):
        if w[k]>w[k+1]:        
            w[k],w[k+1]=w[k+1],w[k]
            print(w)
                    
        
