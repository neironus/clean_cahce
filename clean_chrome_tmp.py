import os
import glob
import subprocess

def get_allprofiles(user):
    profiles_path = f'C:\\Users\\{user}\\AppData\\Local\\Mozilla\\chrome\\Profiles\\*'
    profiles_list = glob.glob(f'{profiles_path}')
    return profiles_list

def kill_chrome():
    #kill all chrome process
    subprocess.call('taskkill /F /IM Chrome.exe', shell=False)
    
def clean_chrome(user_name):
    kill_chrome()
    cache_main    = f'C:\\Users\\{user_name}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache\\*'
    cache_js = f'C:\\Users\\{user_name}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Code Cache\\js\\*'
    caches = [cache_main, cache_js]
    for cache in caches:
        cleaning_files_list = glob.glob(cache)
        for file in cleaning_files_list:
            try:
                os.remove(file)
                print(f"Removed file - {file}")
            except (PermissionError, NotADirectoryError, OSError) as err:
                print(f"Error while deleting file : {file}")
                folder = file
                try:
                    os.rmdir(folder)
                except (NotADirectoryError, OSError):
                    print(f"Error while deleting folder : {folder}")

def main():
    clean_chrome('Max')

if __name__ == "__main__":
    main()