import os
import glob
import subprocess
# import shutil
from pathlib import Path


def encode_string(string):
    try:
        return string.encode(encoding='UTF-8', errors='strict').decode("cp1251")
    except (UnicodeDecodeError, AttributeError):
        return string


def kill_programs():
    # logoff all users except Administrator
    pass
    # kill process
    # subprocess.call('taskkill /F /IM firefox.exe', shell=False)
    # subprocess.call('taskkill /F /IM Chrome.exe', shell=False)
    # subprocess.call('taskkill /F /IM Viber.exe', shell=False)
    # subprocess.call('taskkill /F /IM Skype.exe', shell=False)
    # subprocess.call('taskkill /F /IM 1cv8.exe', shell=False)

files_extensions = ['*_converted.*']

def get_files(users_path, extensions=files_extensions):
    all_files = []
    for ext in extensions:
        all_files.extend(Path(users_path).glob(ext)) # for recursive search use rglob
    return [str(file) for file in all_files]

def clean_converted_files(user_name):
    user_path = f'C:\\Users\\{user_name}\\Documents\\'
    files = get_files(user_path)
    for file in files:
        try:
            os.remove(file)
            print(f'Removed file - {file}')
        except:
            print(f"Error while deleting file : {file}")

def main():
    user_name = "Max"
    clean_converted_files(user_name)



if __name__ == "__main__":
    main()
