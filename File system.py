import os

folder_head_name = "root_folder"

# make the directory
if os.path.exists(folder_head_name):
    pass
else:
    os.makedirs(folder_head_name)

folder_directory = os.getcwd() + "/" + folder_head_name 

# entering the folder and creating folders in it
folder_count = 10

for i in range(folder_count):
    if os.path.exists(folder_directory + "/" + f"folder_{i+1}"):
        pass
    else:
        os.makedirs(folder_directory + "/" + f"folder_{i+1}")
    