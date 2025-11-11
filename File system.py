import os

folder_head_name = "root_folder"

# make the directory
os.makedirs(folder_head_name)

# listing all the folders inside our current directory
for folders in os.listdir(os.curdir):
    print(folders)