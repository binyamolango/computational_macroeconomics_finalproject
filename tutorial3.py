### Tutorial 3: Matplotlib
import matplotlib.pyplot as plt
import numpy as np


# create lists

# draw 100 realizations from standard normal distribution
mylist1 = np.random.normal(size = 100)
mylist2 = np.random.normal(size = 100)
mylist3 = np.random.normal(size = 100)

# draw 100 realizations from a uniformly distributed random variable
# that is bounded by the interval [0,10]
mylist4 = np.random.uniform(0, 10, 100)
mylist5 = np.random.uniform(0, 10, 100)
mylist6 = np.random.uniform(0,10, 100)


# draw 100 realizations from poisson distribution
# side note: the poisson distribution can be used to model count data
mylist7 = np.random.poisson (size = 100)
mylist8 = np.random.poisson (1,100)
mylist9 = np.random.poisson (size = 100)

# make a figure with three subplots below each other
# create fig object with three subplots
# one can apply certain operations to the fig object

















fig, (ax1, ax2, ax3) = plt.subplots(3) 

# first plot, use mylist1-mylist3
plt.subplot(3,1,1)
plt.plot(mylist1, color="green", linestyle="dashed")
plt.plot(mylist2, color="red", linestyle="dotted")
plt.plot(mylist3, color="black", linewidth= 4,linestyle="solid")

plt.title ("Plot with the random numbers from the normal distribution")

# second and third plot, use mylist4-mylist6 and mylist7-mylist9, respectively
plt.subplot(3,1,2)
plt.plot(mylist4, color="cyan", linestyle="dashdot")
plt.plot(mylist5, color="yellow", linestyle="dashdot")
plt.plot(mylist6, color="magenta", linestyle="dashdot")

plt.title("Plot with the random numbers from the uniform distribution")

plt.subplot(3,1,3)
plt.plot(mylist7, color="pink", linestyle="dashed")
plt.plot(mylist8, color="olive", linestyle="dotted")
plt.plot(mylist9, color="grey", linewidth= 2,linestyle="solid")
plt.title("Plot with the random numbers from the Poisson distribution")
plt.xlim(0, 100)

plt.tight_layout() #you need to apply .thight_layout() to the fig object

### primer on other methods to apply options

# give plots a name


fig, (ax1, ax2, ax3) = plt.subplots(3) 

plt.subplot(3,1,1)
line1 = plt.plot(mylist1)
line2 = plt.plot(mylist2)
line3 = plt.plot(mylist3)
plt.title ("Plot with the random numbers from the normal distribution")

line11=line1[0]
line11.set_color("pink") #line1 is a list

# yet another way: set properties for object line1
plt.setp(line1,color='blue')




fig, (ax1, ax2, ax3) = plt.subplots(3) 

# first plot, use mylist1-mylist3
plt.subplot(3,1,1)
plt.plot(xvalues,mylist1, color="green", linestyle="dashed", label='Normal_1')
plt.plot(mylist2, color="red", linestyle="dotted", label='Normal_2')
plt.plot(mylist3, color="black", linewidth= 4,linestyle="solid", label='Normal_3')
plt.legend(loc='center')
plt.title ("Plot with the random numbers from the normal distribution")

# second and third plot, use mylist4-mylist6 and mylist7-mylist9, respectively
plt.subplot(3,1,2)
plt.plot(mylist4, color="cyan", linestyle="dashdot",  label='Uniform_1')
plt.plot(mylist5, color="yellow", linestyle="dashdot",  label='Uniform_2')
plt.plot(mylist6, color="magenta", linestyle="dashdot",  label='Uniform_3')
plt.legend()
plt.title("Plot with the random numbers from the uniform distribution")

plt.subplot(3,1,3)
plt.plot(mylist7, color="pink", linestyle="dashed", label='Poisson_1')
plt.plot(mylist8, color="olive", linestyle="dotted", label='Poisson_2')
plt.plot(mylist9, color="grey", linewidth= 2,linestyle="solid", label='Poisson_3')
plt.title("Plot with the random numbers from the Poisson distribution")
plt.legend(loc='lower left')
plt.tight_layout() #you need to apply .thight_layout() to the fig object
