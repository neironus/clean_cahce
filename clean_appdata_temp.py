import os
from pathlib import Path

files_extensions = ['*.pdf', '*.doc', '*.docx',
                    '*.xls', '*.xlsx', '*.tmp', '*_converted.*']


def get_files(users_path, extensions=files_extensions):
    """
    Функция создает список файлов на основе паттерна из files_extensions.
    rglob делает рекурсивный поиск во всех вложенных каталогах
    если нужно только один уровень, то нужно использовать glob
    """
    all_files = []
    for ext in extensions:
        all_files.extend(Path(users_path).rglob(ext))
    return [str(file) for file in all_files]


def clean_appdata_temp_files(user_name):
    """
    Функция принимает имя пользователя, подставляет его в шаблон,
    проходит по списку файлов и питается удалить его 
    """
    user_path = f'C:\\Users\\{user_name}\\AppData\\Local\\Temp\\'
    files = get_files(user_path)
    for file in files:
        try:
            os.remove(file)
            print(f'Removed file - {file}')
        except:
            print(f"Error while deleting file : {file}")


def main():
    user_name = "Max"
    clean_appdata_temp_files(user_name)


if __name__ == "__main__":
    main()
