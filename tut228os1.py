# tut228os1.py

#OS MODULE 
import os 

# os.getcwd()
print(os.getcwd())    #current working directory cwd
#creating folder
# os.mkdir('movies')
# print(os.path.exists('movies'))

# if os.path.exists('movies'):
#     print("Already exists")
# else:
#     os.mkdir('movies')

# if os.path.exists('song'):
#     print("Already exists")
# else:
#     os.mkdir('song')

#creating file    it's main feature is that it doesn't show error in recreating the same file which shows error in folder creation
open('alina.txt','a')

# An 'r' before a string tells the Python interpreter to treat backslashes as a literal (raw) character. Normally, Python uses backslashes as escape characters.
# os.mkdir(r'D:\al\newfile.txt')   #method to create folder inside the path name given

if os.path.exists(r'D:\al\newfile.txt'):
    print("Already Exists")
else:
    os.mkdir(r'D:\al\newfile.txt') 

#Methods to list the directories of the files
# Method-1
# print(os.listdir())
    
# E:\asdf\python tutorials
# Method-2
# for item in os.listdir(r'E:\Documents\Alina_csit\6th sem\Net Centric Computing'):
#     print(os.path.join(r'E:\Documents\Alina_csit\6th sem\Net Centric Computing',item))

    # print(r'E:\asdf\python tutorials' + '\\'+ item)










