import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
import base64
import os
import json

class GSheets:

    def authenticate(self):
        
        scopes = ['https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive']

        
        decodedBytes = base64.b64decode(os.getenv('SACREDS'))
        sa_info = json.loads(decodedBytes)
        credentials = Credentials.from_service_account_info(sa_info, scopes=scopes)

        return gspread.authorize(credentials)

    def selectSheet(self, gcreds, sheetKey, tab):

        # Open a google sheet
        gs = gcreds.open_by_key(sheetKey)
        # Set sheet
        sheet = gs.worksheet(tab)

        return sheet, gs
    
    def clearSheet(self, sheet):

        # Clear the worksheet
        sheet.clear()

    def setSheet(self, sheet, df):
        # Sets in the Sheet
        set_with_dataframe(worksheet=sheet, dataframe=df, include_index=False, include_column_header=True, resize=True)

    def appendSheet(self, sheet, df, gs):
        # Appends to the sheet
        df_values = df.values.tolist()
        gs.values_append('Steps', {'valueInputOption': 'RAW'}, {'values': df_values})