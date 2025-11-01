# pip install Send2Trash colorama
import os
import send2trash
from colorama import init, Fore, Style

# Activating color support in Windows
init(autoreset=True)

def delete_temp_files(folder_path):
    # Checking for the existence of the folder
    if not os.path.exists(folder_path):
        print(f"{Fore.YELLOW}⚠️ The folder does not exist: {folder_path}{Style.RESET_ALL}")
        return
    
    try:
        # Getting a list of all files and folders inside the folder
        files = os.listdir(folder_path)
    except PermissionError:
        print(f"{Fore.YELLOW}⚠️ Permission denied for folder: {folder_path}{Style.RESET_ALL}")
        return

    # Deleting files and folders
    for file in files:
        file_path = os.path.join(folder_path, file)
        try:
            send2trash.send2trash(file_path)
            print(f"{Fore.GREEN}✅ Transferred {file_path} to the recycle bin.{Style.RESET_ALL}")
        except Exception as e:
            # Messages related to permissions
            if "Access is denied" in str(e) or "PermissionError" in str(type(e)):
                print(f"{Fore.YELLOW}⚠️ Permission denied for {file_path}: {e}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}❌ Failed to transfer {file_path} to the recycle bin: {e}{Style.RESET_ALL}")

# Getting the current username
current_user = os.getenv('USERNAME')

# The folders from which we will delete the files while replacing the username.
temp_folders = [
    "C:\\Windows\\Temp",
    f"C:\\Users\\{current_user}\\AppData\\Local\\Temp",
    "C:\\Windows\\Prefetch"
]

# Executing the deletion
for folder in temp_folders:
    delete_temp_files(folder)
