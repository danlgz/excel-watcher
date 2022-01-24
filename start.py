import eel, random, tkinter, tkinter.filedialog as filedialog
from watcher import Watcher
from directory_helper import select_folder

eel.init('web')
watcher = Watcher()

@eel.expose
def py_select_folder():
    watcher.set_folder_path(select_folder())
    eel.js_reload_dom()()

@eel.expose
def py_get_meta():
    return watcher.__dict__

@eel.expose
def py_start_to_watch():
    watcher.start(lambda f: eel.js_processing_file(f)())
    eel.js_reload_dom()()

@eel.expose
def py_stop_to_watch():
    watcher.stop()
    eel.js_reload_dom()()

eel.start('excel_watcher.html', size=(800, 550), port=9000)
