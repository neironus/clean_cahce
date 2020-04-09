import os
from pathlib import Path

files_extensions = ['*']

def make_cleaning_list():
    windows_tmp = f'C:\\Windows\\Temp\\'
    recycle_bin = f'C:\\$recycle.bin\\'
    cleaning_list = [windows_tmp, recycle_bin]
    return cleaning_list


def get_files(folder_path, extensions=files_extensions):
    all_files = []
    for ext in extensions:
        all_files.extend(Path(folder_path).rglob(ext))
    return [str(file) for file in all_files]


def clean_system_tmp():
    cleaning_folders_list = make_cleaning_list()
    for folder in cleaning_folders_list:
        all_files = get_files(folder)
        for file in all_files:   
            try:
                os.remove(file)
                print(f"Removed file - {file}")
            except:
                print(f"Error while deleting file : {file}")


def main():
    # clean_system_tmp(str(input("Enter users name: ")))
    clean_system_tmp()


if __name__ == "__main__":
    main()
