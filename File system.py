import os

folder_head_name = "root_folder"

# make the directory
if os.path.exists(folder_head_name):
    pass
else:
    os.makedirs(folder_head_name)

folder_directory = os.getcwd() + "/" + folder_head_name 

'''
    Creating a file handling system where users enter a command at a certain root folder
    and delete files, delete folders, or go back to certain folders and enter folders
'''

# defining the file class tree structure 
class Folder:
    def __init__(self, name, prev_folder_directory):
        self.folder_name = name
        self.previous_folder_directory = directory
        self.holding_folders: list[Folder] = []
        self.holding_files: list[str] = []
        self.total_list: list = []
        self.folder_index: int = 0
    
    def current_folder(self, command: str) -> str:
        '''
        return the next folder or file name
        '''
        if command == "up":
            if self.folder_index + 1 > len(self.total_list) - 1:
                return self.total_list[self.folder_index]
            else:
                self.folder_index += 1
                return self.total_list[self.folder_index + 1]
        
        else:
            if self.folder_index - 1 < 0:
                return self.total_list[self.folder_index]
            else:
                self.folder_index -= 1
                return self.total_list[self.folder_index + 1]
            
    def Add_folder(self, folder: Folder):
        self.holding_folders.append(folder) # adding folder to list of folders 
        # renewing the list of folders and files in the current folder
        self.total_list = []
        self.total_list.extend(self.holding_folders)
        self.total_list.extend(self.holding_files)
        
    def Add_file(self, filepath: str):
        self.holding_filess.append(folder) # adding files to list of files 
        # renewing the list of folders and files in the current folder
        self.total_list = []
        self.total_list.extend(self.holding_folders)
        self.total_list.extend(self.holding_files)
        
    
    