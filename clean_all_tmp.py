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
    """
    Функция создает список пользователей которые есть в системе
    и возвращает его
    """
    entries = os.scandir('c:\\Users')
    return [encode_string(entry.name) for entry in entries]


def clean_users_list(users_list):
    """
    Функция исключения пользователей из списка.
    Для исключени пользователя нужно добавить в users_exclusion    
    """
    users_exclusion = ['Default', 'Default User',
                       'All Users', 'Public', 'admin', 'Administrator']
    cleaned_users_list = []
    for user in users_list:
        if os.path.isdir(f'c:\\Users\\{user}') and user not in users_exclusion:
            cleaned_users_list.append(user)
    return cleaned_users_list


def main():
    cleaned_users_list = clean_users_list(users_list())
    clean_system_tmp()
    for user in cleaned_users_list:
        clean_firefox(user)
        clean_chrome(user)
        clean_appdata_temp_files(user)
        clean_converted_files(user)


if __name__ == "__main__":
    main()
