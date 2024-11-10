import gspread
from logging import Logger
from pathlib import Path
from ..Constants.GSheetValues import GSheetValues
from oauth2client.service_account import ServiceAccountCredentials

class GSheetReader:
    def __init__(self, logger: Logger, config, sheetId, subdirectory):
        try:
            self.__logger = logger
            self.__subdirectory = subdirectory
            self.__filename = config["sheet_config"]["credential_file"]

            self.__sheet_name = config["sheet_config"]["sheet_name"]
            self.__start_row = config["sheet_config"]["first_start_row"]
            self.__start_col = config["sheet_config"]["last_start_col"]

            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        
            service_account_credential_file = self.__get_full_file_path()
            creds = ServiceAccountCredentials.from_json_keyfile_name(service_account_credential_file, scope)
            self.__client = gspread.authorize(creds)
            self.__sheet = self.__client.open(self.__sheet_name).get_worksheet(sheetId)
        
        except Exception as e:  
             self.__logger.exception(f"An error occurred while getting sheet: {e}")
    
    def get_current_row_by_bab(self, bab_index):
        bab_sheet = self.__client.open(self.__sheet_name).get_worksheet(GSheetValues.BAB_SHEET_ID)
        bab_current_cell_row = bab_index + GSheetValues.BAB_CURRENT_ROW_OFFSET
        self.__current_row = int(bab_sheet.cell(bab_current_cell_row, GSheetValues.BAB_CURRENT_CELL_COL).value)
        return self.__current_row

    def set_current_row_by_bab(self, bab_index, current_row):
        bab_sheet = self.__client.open(self.__sheet_name).get_worksheet(GSheetValues.BAB_SHEET_ID)
        bab_current_cell_row = bab_index + GSheetValues.BAB_CURRENT_ROW_OFFSET
        bab_sheet.update_cell(bab_current_cell_row, GSheetValues.BAB_CURRENT_CELL_COL, current_row)
        
    def get_root_bab_masder(self, current_row = 0):
        try:
            # Find index from where in every cycle it will start filling data
            start_cell_row = self.__get_starting_sheet_row(current_row)
            self.__current_row = start_cell_row # Save it for next iteration

            bab_value    = self.__sheet.cell(start_cell_row, GSheetValues.BAB_COl).value
            root_value   = self.__sheet.cell(start_cell_row, GSheetValues.ROOT_COl).value
            masder_value = self.__sheet.cell(start_cell_row, GSheetValues.MASDER_COl).value
            
            if self.__is_null_or_empty(masder_value) or self.__is_null_or_empty(root_value) or self.__is_null_or_empty(bab_value):
                return
            
            return (root_value.strip(), bab_value.strip(), masder_value.strip())

        except Exception as e:  
             self.__logger.exception(f"An error occurred while getting masder, root and bab from sheet: {e}")

    @property
    def current_row(self):
        return self.__current_row

    @property
    def sheet(self):
        return self.__sheet

    def __get_full_file_path(self):
        current_directory = Path(__file__).parent
        project_directory = current_directory.parent.parent
        file_directory = project_directory / self.__subdirectory
        file_path = file_directory / self.__filename
        return file_path.resolve()

    def __get_starting_sheet_row(self, current_row):
        if current_row == 0:
            start_cell_row = self.__start_row
        else:
            start_cell_row = current_row

        root_value = self.__sheet.cell(start_cell_row, self.__start_col).value

        if self.__is_null_or_empty(root_value):
            return start_cell_row

        while True:
            start_cell_row += 2
            root_value = self.__sheet.cell(start_cell_row, self.__start_col).value

            if self.__is_null_or_empty(root_value):
                break

        return start_cell_row

    def __is_null_or_empty(self, str):
        return str is None or str == ''
        

