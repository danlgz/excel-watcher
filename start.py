import eel, random, tkinter, tkinter.filedialog as filedialog
from watcher import Watcher

eel.init('web')
watcher = Watcher()

@eel.expose
def py_random():
    return random.random()

@eel.expose
def py_select_folder():
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    watcher.set_folder_path(filedialog.askdirectory())
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
