# OS module(2) and shutil module python

import os
import shutil
os.chdir(r'D:\a_l_n')
# print(os.getcwd())  #cwd -> current working directory

# print(os.listdir())

depth=os.walk(r'D:\a_l_n')   #follow dfs

for current_path, folder_names, file_names in depth:
    print(f'current path: {current_path}')
    print(f'folder names: {folder_names}')
    print(f'file names: {file_names}')

#for removing or deleting folders -> should be only empty folder otherwise there can be error
# os.rmdir('del')

#for deleting folders which has some items i.e not empty
# shutil.rmtree('news')
#rmtree function permanently dlts the file/folders, it doesn't send to the recycle bin.

#Copying folder from one to another folder
#shutil.copytree('folder_to_copy','path_where_to_copy/folder_to_copy')
# shutil.copytree('new','priority/new')

#Copying file from one to another folder
# shutil.copy('list1.cpp','new/priority_copied.cpp')

# #Moving file from one to another folder
# shutil.move('new','a_l_n/new2')

#for creating folder inside folder
# os.makedirs('news/newst/newesttt')







