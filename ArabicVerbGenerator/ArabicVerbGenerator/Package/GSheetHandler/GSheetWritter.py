import gspread
from pathlib import Path
from ..Constants.GSheetValues import GSheetValues 
from oauth2client.service_account import ServiceAccountCredentials

class GSheetWritter:
    def __init__(self):
        try:
            self.subdirectory = "Credentials"
            self.filename = "arabicverbgenerator-ff8d2c424453.json"
        
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        
            service_account_credential_file = self.__get_full_file_path()
            creds = ServiceAccountCredentials.from_json_keyfile_name(service_account_credential_file, scope)
            client = gspread.authorize(creds)
            self.sheet = client.open(GSheetValues.GSHEET_NAME).sheet1 
        
        except Exception as e:  
             print(f"An error occurred while getting sheet: {e}")
    
    def get_root_and_bab(self):
        try:
            # Find index from where in every cycle it will start filling data
            start_cell_row, start_cell_col = self.__get_starting_sheet_row()
            root_start_cell_row = start_cell_row
            root_start_cell_col = start_cell_col - 2
            bab_start_cell_row = start_cell_row
            bab_start_cell_col = start_cell_col - 1

            root_value = self.sheet.cell(root_start_cell_row, root_start_cell_col).value
            bab_value = self.sheet.cell(bab_start_cell_row, bab_start_cell_col).value

            if self.__is_null_or_empty(root_value) or self.__is_null_or_empty(bab_value):
                return

            return (root_value, bab_value)

        except Exception as e:  
             print(f"An error occurred while getting root and bab: {e}")

    def __get_full_file_path(self):
        current_directory = Path(__file__).parent
        project_directory = current_directory.parent.parent
        file_directory = project_directory / self.subdirectory
        file_path = file_directory / self.filename
        return file_path.resolve()

    def __get_starting_sheet_row(self):
        start_cell_row = GSheetValues.PAST_FORM_1ST_PERSON_CELL_ROW
        start_cell_col = GSheetValues.PAST_FORM_1ST_PERSON_CELL_COL

        root_value = self.sheet.cell(start_cell_row, start_cell_col).value

        if self.__is_null_or_empty(root_value):
            return (start_cell_row, start_cell_col)

        while True:
            start_cell_row += 2
            root_value = self.sheet.cell(start_cell_row, start_cell_col).value

            if self.__is_null_or_empty(root_value):
                break

        return (start_cell_row, start_cell_col)

    def __is_null_or_empty(self, str):
        return str is None or str == ''
        

