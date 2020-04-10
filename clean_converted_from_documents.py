import os
import glob
from pathlib import Path


files_extensions = ['*_converted.*']


def get_files(users_path, extensions=files_extensions):
    """
    Функция создает список файлов на основе паттерна из files_extensions.
    rglob делает рекурсивный поиск во всех вложенных каталогах
    glob делает поиск в корне данного каталога (только один уровень)
    """
    all_files = []
    for ext in extensions:
        all_files.extend(Path(users_path).glob(ext))
    return [str(file) for file in all_files]


def clean_converted_files(user_name):
    """
    Функция принимает имя пользователя и удаляет файлы с папки 
    C:\\Users\\{user_name}\\Documents\\ 
    найденные по шаблону из files_extensions с помощью функции get_files  
    """
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
