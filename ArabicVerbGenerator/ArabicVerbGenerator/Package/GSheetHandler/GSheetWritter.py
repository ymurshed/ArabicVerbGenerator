import gspread
from gspread.worksheet import Worksheet
from ..Constants.GSheetValues import GSheetValues

class GSheetWritter:
    def __init__(self, sheet: Worksheet, current_row, past_forms, present_forms):
        self._sheet = sheet
        self._current_row = current_row
        self._past_forms = past_forms
        self._present_forms = present_forms
        
    def write_forms(self):
        try:
           self.__write_past_forms()
           self.__write_present_forms()

        except Exception as e:  
             print(f"An error occurred while writting forms in sheet: {e}")            

    def __write_past_forms(self):
        row = self._current_row
        col = GSheetValues.PAST_FORM_3RD_PERSON_CELL_COL
        self._sheet.update_cell(row, col, self._past_forms[0])
        row = self._current_row + 1
        self._sheet.update_cell(row, col, self._past_forms[1])

        row = self._current_row
        col = GSheetValues.PAST_FORM_2ND_PERSON_CELL_COL
        self._sheet.update_cell(row, col, self._past_forms[2])
        row = self._current_row + 1
        self._sheet.update_cell(row, col, self._past_forms[3])

        row = self._current_row
        col = GSheetValues.PAST_FORM_1ST_PERSON_CELL_COL
        self._sheet.update_cell(row, col, self._past_forms[4])
        
    def __write_present_forms(self):
        row = self._current_row
        col = GSheetValues.PRESENT_FORM_3RD_PERSON_CELL_COL
        self._sheet.update_cell(row, col, self._present_forms[0])
        row = self._current_row + 1
        self._sheet.update_cell(row, col, self._present_forms[1])

        row = self._current_row
        col = GSheetValues.PRESENT_FORM_2ND_PERSON_CELL_COL
        self._sheet.update_cell(row, col, self._present_forms[2])
        row = self._current_row + 1
        self._sheet.update_cell(row, col, self._present_forms[3])

        row = self._current_row
        col = GSheetValues.PRESENT_FORM_1ST_PERSON_CELL_COL
        self._sheet.update_cell(row, col, self._present_forms[4])