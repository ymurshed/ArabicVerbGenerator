import gspread
from gspread.worksheet import Worksheet
from ..Constants.GSheetValues import GSheetValues

class GSheetWritter:
    def __init__(self, sheet: Worksheet, current_row, 
                 past_forms, present_forms, negative_past_forms, negative_present_forms,  
                 order_forms, forbid_forms, negative_future_forms, for_present_forms, object_forms):
        
        self.__sheet                    = sheet
        self.__current_row              = current_row
        self.__past_forms               = past_forms
        self.__present_forms            = present_forms
        self.__negative_past_forms      = negative_past_forms
        self.__negative_present_forms   = negative_present_forms
        self.__order_forms              = order_forms
        self.__forbid_forms             = forbid_forms
        self.__negative_future_forms    = negative_future_forms
        self.__for_present_forms        = for_present_forms
        self.__object_forms             = object_forms
    
    def _is_cell_blank(self, col):
        cell_val = self.__sheet.cell(self.__current_row, col).value
        return cell_val is None or cell_val == ''

    def write_forms(self):
        try:
            if self._is_cell_blank(GSheetValues.PAST_FORM_3RD_PERSON_CELL_COL):
                self.__write_past_forms()

            if self._is_cell_blank(GSheetValues.PRESENT_FORM_3RD_PERSON_CELL_COL):
                self.__write_present_forms()

            if self._is_cell_blank(GSheetValues.NEGATIVE_PAST_FORM_3RD_PERSON_CELL_COL):
                self.__write_negative_past_forms()

            if self._is_cell_blank(GSheetValues.NEGATIVE_PRESENT_FORM_3RD_PERSON_CELL_COL):
                self.__write_negative_present_forms()

            if self._is_cell_blank(GSheetValues.ORDER_FORM_2ND_PERSON_CELL_COL):
                self.__write_order_forms()
            
            if self._is_cell_blank(GSheetValues.FORBID_FORM_2ND_PERSON_CELL_COL):
                self.__write_forbid_forms()
            
            if self._is_cell_blank(GSheetValues.NEGATIVE_FUTURE_FORM_3RD_PERSON_CELL_COL):
                self.__write_negative_future_forms()

            if self._is_cell_blank(GSheetValues.FOR_PRESENT_FORM_3RD_PERSON_CELL_COL):
                self.__write_for_present_forms()
            
            if self._is_cell_blank(GSheetValues.OBJECT_PAST_FORM_3RD_PERSON_CELL_COL):
                self.__write_object_forms()

        except Exception as e:  
             print(f"An error occurred while writting forms in sheet: {e}")            
    
    def __write_past_forms(self):
        row = self.__current_row
        col = GSheetValues.PAST_FORM_3RD_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__past_forms[0])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__past_forms[1])

        row = self.__current_row
        col = GSheetValues.PAST_FORM_2ND_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__past_forms[2])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__past_forms[3])

        row = self.__current_row
        col = GSheetValues.PAST_FORM_1ST_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__past_forms[4])
    
    def __write_present_forms(self):
        row = self.__current_row
        col = GSheetValues.PRESENT_FORM_3RD_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__present_forms[0])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__present_forms[1])

        row = self.__current_row
        col = GSheetValues.PRESENT_FORM_2ND_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__present_forms[2])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__present_forms[3])

        row = self.__current_row
        col = GSheetValues.PRESENT_FORM_1ST_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__present_forms[4])

    def __write_negative_past_forms(self):
        row = self.__current_row
        col = GSheetValues.NEGATIVE_PAST_FORM_3RD_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__negative_past_forms[0])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__negative_past_forms[1])

        row = self.__current_row
        col = GSheetValues.NEGATIVE_PAST_FORM_2ND_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__negative_past_forms[2])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__negative_past_forms[3])

        row = self.__current_row
        col = GSheetValues.NEGATIVE_PAST_FORM_1ST_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__negative_past_forms[4])
    
    def __write_negative_present_forms(self):
        row = self.__current_row
        col = GSheetValues.NEGATIVE_PRESENT_FORM_3RD_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__negative_present_forms[0])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__negative_present_forms[1])

        row = self.__current_row
        col = GSheetValues.NEGATIVE_PRESENT_FORM_2ND_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__negative_present_forms[2])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__negative_present_forms[3])

        row = self.__current_row
        col = GSheetValues.NEGATIVE_PRESENT_FORM_1ST_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__negative_present_forms[4])

    def __write_order_forms(self):
        row = self.__current_row
        col = GSheetValues.ORDER_FORM_2ND_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__order_forms[0])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__order_forms[1])

    def __write_forbid_forms(self):
        row = self.__current_row
        col = GSheetValues.FORBID_FORM_2ND_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__forbid_forms[0])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__forbid_forms[1])

    def __write_negative_future_forms(self):
        row = self.__current_row
        col = GSheetValues.NEGATIVE_FUTURE_FORM_3RD_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__negative_future_forms[0])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__negative_future_forms[1])

        row = self.__current_row
        col = GSheetValues.NEGATIVE_FUTURE_FORM_2ND_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__negative_future_forms[2])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__negative_future_forms[3])

        row = self.__current_row
        col = GSheetValues.NEGATIVE_FUTURE_FORM_1ST_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__negative_future_forms[4])

    def __write_for_present_forms(self):
        row = self.__current_row
        col = GSheetValues.FOR_PRESENT_FORM_3RD_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__for_present_forms[0])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__for_present_forms[1])

        row = self.__current_row
        col = GSheetValues.FOR_PRESENT_FORM_2ND_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__for_present_forms[2])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__for_present_forms[3])

        row = self.__current_row
        col = GSheetValues.FOR_PRESENT_FORM_1ST_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__for_present_forms[4])

    def __write_object_forms(self):
        # Past forms
        row = self.__current_row
        col = GSheetValues.OBJECT_PAST_FORM_3RD_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__object_forms[0])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__object_forms[1])

        row = self.__current_row
        col = GSheetValues.OBJECT_PAST_FORM_2ND_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__object_forms[2])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__object_forms[3])

        row = self.__current_row
        col = GSheetValues.OBJECT_PAST_FORM_1ST_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__object_forms[4])

        # Present forms
        row = self.__current_row
        col = GSheetValues.OBJECT_PRESENT_FORM_3RD_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__object_forms[5])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__object_forms[6])

        row = self.__current_row
        col = GSheetValues.OBJECT_PRESENT_FORM_2ND_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__object_forms[7])
        row = self.__current_row + 1
        self.__sheet.update_cell(row, col, self.__object_forms[8])

        row = self.__current_row
        col = GSheetValues.OBJECT_PRESENT_FORM_1ST_PERSON_CELL_COL
        self.__sheet.update_cell(row, col, self.__object_forms[9])