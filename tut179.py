# define generator function
# take one number as argument
# generate a sequence of even numbers from 1 to that number
def even_gen(num):
    # for i in range(1,num+1):
    #     if i%2==0:
      for i in range(1,num+1,2):      
            yield(i)

# print(even(10))
n=even_gen(20)
for numb in n:
    print(numb)
for numb in n:
    print(numb)