from __future__ import annotations 
import os


'''
    Creating a file handling system where users enter a command at a certain root folder
    and delete files, delete folders, or go back to certain folders and enter folders
'''

# defining the file class tree structure 
class Folder:
    def __init__(self, name, prev_folder_directory, prev_folder):
        self.name = name
        self.previous_folder_directory = prev_folder_directory
        self.previous_folder = prev_folder
        self.holding_folders: list[Folder] = []
        self.folder_index: int = 0
    
    def get_pointed_subfolder(self, command: str) -> None:
        '''
        return the next folder or file name
        '''
        if command == "down":
            if self.folder_index + 1 > len(self.holding_folders) - 1:
                return 
            else:
                self.folder_index += 1
        
        elif command == "up":
            if self.folder_index - 1 < 0:
                return 
            else:
                self.folder_index -= 1
            
        else:
            return 
            
    def Add_folder(self, folder: Folder) -> None :
        self.holding_folders.append(folder) # adding folder to list of folders 
        
    def display_content(self) -> None:
        # showing all contents of the folder 
        for idx, content in enumerate(self.holding_folders):
            if self.folder_index == idx:
                print("--> ")
                print(content.name)
            else:
                print(f"{idx + 1}. ")
                print(content.name)
                
    def enter_pointed_subfolder(self) -> any:
        return self.holding_folders[self.folder_index]
        
def clear_screen():
    os.system('cls')
    
def __file_system__(root_folder: Folder) -> None:
    current_folder: Folder = root_folder 
    
    current_folder.display_content()
    previous_directory = os.getcwd() + "/" + current_folder.name
    
    command = '0'
    
    while command.strip().lower() != "quit":
        
        if command.strip().lower() == "create":
            name = input("name: ")
            
            clear_screen()
            current_name = previous_directory + "/" + name
            new_folder = Folder(current_name, prev_folder_directory=previous_directory, prev_folder=current_folder)
            current_folder.Add_folder(new_folder)
            current_folder.display_content()

        if command.strip().lower() == "up":
            clear_screen()
            pointed_subfolder = current_folder.get_pointed_subfolder("up")
            current_folder.display_content()
            
        if command.strip().lower() == "down":
            clear_screen()
            current_folder.get_pointed_subfolder("down")
            current_folder.display_content()
            
        if command.strip().lower() == "enter":
            clear_screen()
            current_folder = current_folder.enter_pointed_subfolder()
            previous_directory = current_folder.name
            current_folder.display_content()
            
        if command.strip().lower() == "back":
            clear_screen()
            current_folder = current_folder.previous_folder
            if previous_directory: 
                previous_directory = current_folder.previous_folder_directory
                current_folder.display_content()
            else:
                pass 
            
        command = str(input("Enter command: "))
            
            
if __name__ == "__main__":
    root_folder = Folder("/test", "None", None)
    __file_system__(root_folder)
            
                
            
    