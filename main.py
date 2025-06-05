import os
from auth import GarminAuth
from api import GarminAPI
from datetime import date, timedelta
from dotenv import load_dotenv
import pandas as pd
from gsheets import GSheets

# Refresh dotenv
load_dotenv(override=True)

# Set yesterday in iso format
TwentyEightDaysAgo = date.today() - timedelta(days=28)
yesterday = date.today() - timedelta(days=1)
yesterday = yesterday.isoformat()

# Login
garmin = GarminAuth(
    email = os.getenv("EMAIL"),
    password = os.getenv("PASS"),
    tokenstore = os.getenv("GARMINTOKENS")
)

garmin.login()

# Instantiate API
api = GarminAPI()

# Instantiate Google Sheets
gsheets = GSheets()

# Get steps from yesterday
# steps = garmin.connectapi("/usersummary-service/stats/steps/daily/2025-06-03/2025-06-03")
url = api.get_daily_steps(yesterday, yesterday)
steps = garmin.connectapi(url)

# Set steps in Pandas DataFrame
df = pd.DataFrame(steps)
# Delete rows with NaN
df = df.dropna()

# Google Sheets
gc = gsheets.authenticate()

# Select sheet
sheet, gs = gsheets.selectSheet(gc, os.getenv('SHEETKEY'), 'Steps')

# Append yesterday's steps to the sheet
gsheets.appendSheet(sheet, df, gs)