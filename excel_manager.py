from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException
from directory_helper import move_file


class ExcelManager:
    _base_path = None
    processed_folder_name = '_processed'
    not_processed_folder_name = '_not_processed'
    result_folder_name = '_result'
    folders = [processed_folder_name, not_processed_folder_name, result_folder_name]

    def _get_absolute_path(self, concat=''):
        return f'{self._base_path}/{concat}'

    def _ignore_file(self, file):
        move_file(self._get_absolute_path(file), self._get_absolute_path(f'{self.not_processed_folder_name}/{file}'))

    def set_base_path(self, path):
        self._base_path = path

    def process(self, file):
        if not self._base_path:
            raise 'Base path is required'

        try:
            wb = load_workbook(self._get_absolute_path(file))
        except InvalidFileException:
            self._ignore_file(file)
            print('invalid file:', file)
            return
