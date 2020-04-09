import os
from clean_firefox_tmp import clean_firefox
from clean_chrome_tmp import clean_chrome
from clean_system_tmp import clean_system_tmp
from clean_appdata_temp import clean_appdata_temp_files
from clean_converted_from_documents import clean_converted_files

def encode_string(string):
    try:
        return string.encode(encoding='UTF-8', errors='strict').decode("cp1251")
    except (UnicodeDecodeError, AttributeError):
        return string


def users_list():
    entries = os.scandir('c:\\Users')
    return [encode_string(entry.name) for entry in entries]


def clean_users_list(users_list):
    users_exclusion = ['Default', 'Default User',
                       'All Users', 'Public', 'admin', 'Administrator']
    cleaned_users_list = []
    for user in users_list:
        if os.path.isdir(f'c:\\Users\\{user}') and user not in users_exclusion:
            cleaned_users_list.append(user)
    return cleaned_users_list


def main():
    cleaned_users_list = clean_users_list(users_list())
    clean_system_tmp() # updated
    # kill firefox and other once
    for user in cleaned_users_list:
        clean_firefox(user) # need update
        clean_chrome(user) # need update
        clean_appdata_temp_files(user) # updated
        clean_converted_files(user) # updated

if __name__ == "__main__":
    main()
