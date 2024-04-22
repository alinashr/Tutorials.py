# Define  is_palindrome function that take one word 
# in string as input and return True if it is palidrome else return False

# logic (algorithm)
# step-1 -> reverse the string 
# step-2 -> compare reverrsed string with the original string

def is_palindrom(word):
    reverse=string[::-1]
    if word==reverse:
        return True 
    return False
    
string =input("Enter any string : ")
# print(string[0])
# print(reverse)
print(is_palindrom(string))



