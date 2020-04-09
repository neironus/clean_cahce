import os
import glob
import subprocess



def encode_string(string):
    try:
        return string.encode(encoding='UTF-8',errors='strict').decode("cp1251")
    except (UnicodeDecodeError, AttributeError):
        return string 

def get_allprofiles(user):
    profiles_path = f'C:\\Users\\{user}\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\*'
    profiles_list = glob.glob(f'{profiles_path}')
    return profiles_list

def make_cleaning_list(profiles_list):
    # Windows 10+
    cache = '\\cache2\\entries\\*'
    thumbnails = '\\thumbnails\\*'
    cleaning_list = []
    for profile in profiles_list:
        cleaning_list.append(profile + cache)
        cleaning_list.append(profile + thumbnails)
    return cleaning_list

def kill_firefox():
    #kill all firefox process
    try:
        subprocess.call('taskkill /F /IM firefox.exe', shell=False)
    except:
        pass
    
def clean_firefox(user_name):
    profiles_list = get_allprofiles(user_name)
    cleaning_folders_list = make_cleaning_list(profiles_list)
    for folder in cleaning_folders_list:
        all_files = glob.glob(folder)
        for file in all_files:
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
    kill_firefox()
    clean_firefox('Max')

if __name__ == "__main__":
    main()