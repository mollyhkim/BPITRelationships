from __future__ import print_function
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json
import csv
import numpy as np
import tensorflow as tf


SCOPE = ["https://spreadsheets.google.com/feeds"]
SECRETS_FILE = "Salesforce Data-6c84ebef2ffc.json"
SPREADSHEET = "Salesforce data"

json_key = json.load(open(SECRETS_FILE))
# Authenticate using the signed key
credentials = ServiceAccountCredentials.from_json_keyfile_name(SECRETS_FILE, SCOPE)

gc = gspread.authorize(credentials)
#print("The following sheets are available")
#for sheet in gc.openall():
#    print("{} - {}".format(sheet.title, sheet.id))

workbook = gc.open(SPREADSHEET)
sheet = workbook.sheet1
COLUMNS = []#sheet.row_values(1)
all_cells=sheet.range('A1:I1')
for cell in all_cells:
    COLUMNS.append(cell.value)
print(COLUMNS)
CATEGORICAL_COLUMNS = [sheet.acell('B1').value,sheet.acell('G1').value]
#may also need to include "num_won", "num_lost" as continuous
CONTINUOUS_COLUMNS = [sheet.acell('C1').value, sheet.acell('H1').value,sheet.acell('I1').value]

print("CATEGORICAL")
print(CATEGORICAL_COLUMNS)
print("CONTINUOUS")
print(CONTINUOUS_COLUMNS)
data = pd.DataFrame(sheet.get_all_records()).values
print("-------------DATA----------------")
data=data.tolist()
data=list(reversed(data))
for i in (reversed(data)):
    print(i)


