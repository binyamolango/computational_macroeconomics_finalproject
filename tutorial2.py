### Tutorial 2

import numpy as np


### Exercise 1.1

#create a 20 x 20 matrix
a = np.zeros ((20,20))

# assign values in ascending order to columns (1-10) by slicing method
a[:,0] = 1
a[:,1] = 2
a[:,2] = 3
a[:,3] = 4
a[:,4] = 5
a[:,5] = 6
a[:,6] = 7
a[:,7] = 8
a[:,8] = 9
a[:,9] = 10

print(a)



# with for-loop
a = np.zeros ((20,20))

for i in range(10):
    a[:,i] = i+1
print(a)



#with np arange and for loop
a = np.zeros ((20,20))

for i in range(20):
    a[i,:10] = np.arange(1,11)
print(a)


#with np arange without a loop
a = np.zeros ((20,20))
a[:,:10] = np.arange(1,11)
print(a)


# assign the right half of matrix (column 11-20) realizations from
# normal distribution
for i in range(20):
    a[i,10:20] = np.random.randn(10)
print(a)



for i in range(10,20):
    a[:,i]= np.random.randn(20)
print(a)


#without a loop
a[:,10:]=np.random.normal(size=(20, 10))
print(a)

np.random.normal(size=(20, 10))

np.set_printoptions(precision=2)
print(a)








#slice the values that we need and print a sum 
b = a[3:14, 2:9]


print(b)
print (b.sum())
print(np.sum(b,axis=0))


print (sum(sum(b)))
print (b.sum(0))
print (b.sum(1))


#change the value of the 6th row
print(a[5,:])
a[5,:] = a[1,:]+a[19,:]
print(a[5,:])







#change values, you need to loop over all rows and columns        
for i in range (20):
    for r in range(10,20):       
        if a[i,r] > 0.2:
            a[i,r] = a[i,1]
        elif a[i,r] < -0.2:
            a[i,r] = a[i,5]
        else:
            a[i,r] = a[i,8]          
print(a)
        



#Or alternatively without a loop using the np.where function
index1 = np.where(a[:, 10:20] > 0.2)
a[index1[0], index1[1] + 10] = a[index1[0], 1]

index2 = np.where(a[:, 10:20] < -0.2)
a[index2[0], index2[1] + 10] = a[index2[0], 5]

index3 = np.where((a[:, 10:20] > -0.2) & (a[:, 10:20] < 0.2))
a[index3[0], index3[1] + 10] = a[index3[0], 8]


print(a)








#calculate sum of columns
print(a.sum(axis=0))


#alternatively with loop
for i in range(20):
    print(sum(a[:,i]))


#calculate mean of rows
print(a.mean(axis=1))



#alternatively 
for i in range(20):
    print(np.mean(a[i,:]))



### Exercise 1.2


#create a new matrix
new_matrix = a[:,:7] #20x7 matrix
print(new_matrix)

# create a dot product
# 20x20 times 20x7 matrix gives 20x7 matrix
dot_matrix = np.dot(a,new_matrix)
print(dot_matrix)
dot_matrix.size # how many entries?
dot_matrix.shape # dimension?

#delete rows
dot_matrix_dr = np.delete(dot_matrix, (2,3), axis=0)
print(dot_matrix_dr)
dot_matrix_dr.shape # now we are two rows short


#sort elements (in ascending order) in column
dot_matrix_dr[:,4]=np.sort(dot_matrix_dr[:, 4])
print(dot_matrix_dr)

# sort in descending order
y=np.sort(dot_matrix_dr[:, 4]) 
dot_matrix_dr[:,4] = np.flip(y) # np.flip() needs to know that there is only one dimension, i.e. axis=0
print(dot_matrix_dr)

