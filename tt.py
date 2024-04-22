#an
import random
import numpy 
import pylab
#defining number of steps
n = 1000 # n is the number of steps

def random_steps():
    step_size = random.random()
    return step_size
    """ Here 1.0 is the maximum step that a drunk person can take and 0.0 is the least step"""

x = numpy.zeros(n) 
y = numpy.zeros(n) 

for i in range(n):
    step = random.choice(['N', 'S', 'E', 'W'])
    if step == 'N':
        x[i] = x[i - 1] 
        y[i] = y[i - 1] + rand_steps()
    elif step == 'S':
        x[i] = x[i - 1] 
        y[i] = y[i - 1] - rand_steps()
    elif step == 'E':
        x[i] = x[i - 1] + rand_steps()
        y[i] = y[i - 1] 
    else:
        x[i] = x[i - 1] - rand_steps()
        y[i] = y[i - 1]

distance = numpy.add(x,y)

print(distance)
pylab.title("Random Walk 2-D")
pylab.plot(x, y) #plotting
pylab.show()