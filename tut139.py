#sets comprehension - very least used
# set and dictinary has no any order
square={i*i for i in range(1,11)}
print(square)

names={'alna','dff','ioo'}
first_letter={name[0] for name in names}
print(first_letter)     #--> From this we can see that set is an unordered collection   {'d', 'i', 'a'}   