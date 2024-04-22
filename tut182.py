# List vs Generators
# memory usage, and when to use list and when to use generator

import time
# t1=time.time()
# l=[i**2 for i in range(10000000)]
# print(time.time()-t1)
t1=time.time()
g=(i**2 for i in range(10000000))
print(time.time()-t1)

# when to use list?
# to work with the sequence















