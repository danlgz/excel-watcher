from set_queue import SetQueue
from excel_manager import ExcelManager
import os, threading, time


class Watcher:
    folder_path = None
    is_watching = False
    files_queue = SetQueue()
    manager = ExcelManager()

    def set_folder_path(self, path):
        self.folder_path = path
        self.manager.set_base_path(self.folder_path)

    def _start_to_watch(self):
        before = dict([(f, None) for f in os.listdir(self.folder_path)])
        while True:
            if not self.is_watching:
                break
            after = dict([(f, None) for f in os.listdir(self.folder_path)])
            added = [f for f in after if not f in before]
            for file in added:
                if file in self.manager.folders:
                    continue
                print('new file:', self.folder_path, file)
                self.files_queue.put(file)
            before = after

    def _consume_the_queue(self, processing_file_callback=lambda f: f):
        while True:
            if not self.is_watching and self.files_queue.qsize() == 0:
                break
            if self.files_queue.qsize() > 0:
                file = self.files_queue.get()
                self.manager.process(file)
                processing_file_callback(file)

    def start(self, processing_file_callback=lambda f: f):
        if self.folder_path is None:
            raise 'folder path is required'
        self.is_watching = True
        w = threading.Thread(target=self._start_to_watch)
        w.start()
        p = threading.Thread(target=self._consume_the_queue, args=(processing_file_callback,))
        p.start()

    def stop(self):
        if not self.is_watching:
            print('watcher not has started')
            return
        self.is_watching = False
