import os
from dataclasses import dataclass 

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

@dataclass 
class File:
    name: str

# defining the file class tree structure 
class Folder:
    def __init__(self, name, prev_folder_directory, prev_folder):
        self.name = name
        self.previous_folder_directory = directory
        self.previous_folder = 
        self.holding_folders: list[Folder] = []
        self.holding_files: list[File] = []
        self.total_list: list = []
        self.folder_index: int = 0
    
    def get_pointed_subfolder(self, command: str) -> str:
        '''
        return the next folder or file name
        '''
        if command == "up":
            if self.folder_index + 1 > len(self.total_list) - 1:
                return self.total_list[self.folder_index].name
            else:
                self.folder_index += 1
                return self.total_list[self.folder_index + 1].name
        
        else:
            if self.folder_index - 1 < 0:
                return self.total_list[self.folder_index].name
            else:
                self.folder_index -= 1
                return self.total_list[self.folder_index + 1].name
            
    def Add_folder(self, folder: Folder) -> None :
        self.holding_folders.append(folder) # adding folder to list of folders 
        # renewing the list of folders and files in the current folder
        self.total_list = []
        self.total_list.extend(self.holding_folders)
        self.total_list.extend(self.holding_files)
        
    def Add_file(self, filepath: File) -> None:
        self.holding_filess.append(File) # adding files to list of files 
        # renewing the list of folders and files in the current folder
        self.total_list = []
        self.total_list.extend(self.holding_folders)
        self.total_list.extend(self.holding_files)
        
    def display_content(self) -> None:
        # showing all contents of the folder 
        for idx, content in enumerate(self.total_list):
            if self.folder_index == idx:
                print("--> ")
            else:
                print(content.name, "\n")
                
    def enter_pointed_subfolder(self) -> any:
        return self.total_list[self.folder_index]
        
def clear_screen():
    os.system('cls')
    
def __file_system__(root_folder: Folder) -> None:
    current_folder: Folder = root_folder 
    
    current_folder.display_content()
    previous_directory = os.getcwd() + "/" + current_folder.name
    current_path = os.getcwd()
    
    command = str(input("Enter command: "))
    
    while command.lower != "quit":
        
        if command.lower == "create":
            option = int(input("1. Folder \n 2. File"))
            name = input("name: ")
            
            if option == 1:
                clear_screen()
                new_folder = Folder(name, prev_folder_directory=previous_directory)
                current_folder.Add_folder(new_folder)
                current_folder.display_content()
                
            if option == 2:
                clear_screen()
                file_path = current_path + "/" + name + ".txt"
                new_file = File(file_path)
                current_folder.Add_File(new_file)
                current_folder.display_content()
                
        if command.lower == "up":
            clear_screen()
            pointed_subfolder = current_folder.get_pointed_subfolder("up")
            current_folder.display_content()
            
        if command.lower == "down":
            clear_screen()
            pointed_subfolder = current_folder.get_pointed_subfolder("down")
            current_folder.display_content()
            
        if command.lower == "enter":
            
            
                
            
    