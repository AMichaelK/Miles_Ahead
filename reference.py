# %%
import garth
import os
from dotenv import load_dotenv
import datetime
import pandas as pd

# Refresh dotenv
load_dotenv(override=True)

# Login
# Try to resume Garth from file, if not, login
if garth.resume("~/.garth"):
    pass
else:
    garth.login(os.getenv('EMAIL'), os.getenv('PASS'))

# %%

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
twoDaysAgo = today - datetime.timedelta(days=2)

print(today)
print(yesterday)
print(twoDaysAgo)

# %%
start = twoDaysAgo
end = yesterday
garmin_connect_daily_stats_steps_url = ("/usersummary-service/stats/steps/daily")
url = f"{garmin_connect_daily_stats_steps_url}/{start}/{end}"

steps = garth.connectapi(url)

print(steps)

# %% 
# Stick into a Pandas Dataframe and Clean

df = pd.DataFrame(steps)
df = df.dropna()

print(df)

# %%
# Connect to GSheets
from google.oauth2.service_account import Credentials
import gspread
from dotenv import load_dotenv

load_dotenv(override=True)

scopes = ['https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive']


credentials = Credentials.from_service_account_file(os.getenv('SACREDS'), scopes=scopes)
gc = gspread.authorize(credentials)

# %%
# Select Worksheet and Tab

gs = gc.open_by_key(os.getenv('SHEETKEY'))
sheet = gs.worksheet('Steps')

# %% 
# Append DataFrame and GSheets Tab
df_values = df.values.tolist()
gs.values_append('Steps', {'valueInputOption': 'RAW'}, {'values': df_values})
# %%
