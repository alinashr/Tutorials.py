

# def a function
# input list to function
# returns list with first letter capital
# output = ['Hari','Shyam','Ramesh']
list=['hari','shyam','ramesh']
def func(lst,**kwargs):
    if kwargs.get('rev_str')==True:
        return [i[::-1].title()    for i in lst]

    else:
        return [i.title() for i in lst]
    

print(func(list,rev_str=True))
# func(list)







