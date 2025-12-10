# pip install Send2Trash colorama
import os
import send2trash
from colorama import init, Fore, Style

# Activating color support in Windows
init(autoreset=True)

def get_size(path):
    """Calculate the size of file or folder in bytes"""
    total_size = 0
    try:
        if os.path.isfile(path):
            total_size = os.path.getsize(path)
        elif os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    try:
                        total_size += os.path.getsize(filepath)
                    except (OSError, FileNotFoundError):
                        pass
    except (OSError, FileNotFoundError):
        pass
    return total_size

def delete_temp_files(folder_path):
    # Checking for the existence of the folder
    if not os.path.exists(folder_path):
        print(f"{Fore.YELLOW}⚠️ The folder does not exist: {folder_path}{Style.RESET_ALL}")
        return 0
    
    try:
        # Getting a list of all files and folders inside the folder
        files = os.listdir(folder_path)
    except PermissionError:
        print(f"{Fore.YELLOW}⚠️ Permission denied for folder: {folder_path}{Style.RESET_ALL}")
        return 0

    # Variable to track total size of deleted files
    total_deleted_size = 0

    # Deleting files and folders
    for file in files:
        file_path = os.path.join(folder_path, file)
        try:
            # Calculate file size before deletion
            file_size = get_size(file_path)
            send2trash.send2trash(file_path)
            total_deleted_size += file_size
            print(f"{Fore.GREEN}✅ Transferred {file_path} to the recycle bin.{Style.RESET_ALL}")
        except Exception as e:
            # Messages related to permissions
            if "Access is denied" in str(e) or "PermissionError" in str(type(e)):
                print(f"{Fore.YELLOW}⚠️ Permission denied for {file_path}: {e}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}❌ Failed to transfer {file_path} to the recycle bin: {e}{Style.RESET_ALL}")
    
    return total_deleted_size

# Getting the current username
current_user = os.getenv('USERNAME')

# The folders from which we will delete the files while replacing the username.
temp_folders = [
    "C:\\Windows\\Temp",
    f"C:\\Users\\{current_user}\\AppData\\Local\\Temp",
    "C:\\Windows\\Prefetch"
]

# Executing the deletion
total_cleaned = 0
for folder in temp_folders:
    total_cleaned += delete_temp_files(folder)

# Convert bytes to megabytes and display the result
total_mb = total_cleaned / (1024 * 1024)
print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
print(f"{Fore.GREEN}✨ Total cleaned: {total_mb:.2f} MB{Style.RESET_ALL}")
print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}\n")

# Wait for user to press Enter
input(f"{Fore.YELLOW}Press Enter to exit...{Style.RESET_ALL}")
