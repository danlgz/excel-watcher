import os, shutil, tkinter, tkinter.filedialog as filedialog


def is_file(file):
    return os.path.isfile(file)

def move_file(origin, destiny):
    create_directory(destiny)
    shutil.move(origin, destiny)

def create_directory(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def select_folder():
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    return filedialog.askdirectory()
