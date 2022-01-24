import os
import shutil

def move_file(origin, destiny):
    create_directory(destiny)
    shutil.move(origin, destiny)

def create_directory(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
