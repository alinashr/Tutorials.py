import numpy as np
import matplotlib.pyplot as plt
import random
#defining n = 1000
n=1000
def randomwalk2D(n):
    # [0, 0, 0, ... ,0]
    x = np.zeros(n)
    y = np.zeros(n)
    
for i in range(1, n):
        # Pick a direction at random
    directions = ["UP", "DOWN", "LEFT", "RIGHT"]
    step = random.choice(directions)
        
        # Move the object according to the direction
    if step == "RIGHT":
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
        
    elif step == "LEFT":
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif step == "UP":
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    elif step == "DOWN":
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1
    
#   # Return all the x and y positions of the object
    # return x, y
# Here is an example run of a 2D random walk with 1000 steps.

x_data, y_data = randomwalk2D(1000)
plt.title("2D Random Walk in Python")
plt.plot(x_data, y_data)
plt.show()

distance = np.add(x_data,y_data)
print(distance)
