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
today = date.today()

# Login
garmin = GarminAuth(
    email=os.getenv("EMAIL"),
    password=os.getenv("PASS")
)

garmin.login()

# Instantiate API
api = GarminAPI()

# Instantiate Google Sheets
gsheets = GSheets()

#############################################################################
# Get steps from yesterday
url = api.get_daily_steps(yesterday, yesterday)
steps = garmin.connectapi(url)

# Set steps in Pandas DataFrame
df = pd.DataFrame(steps)
# # Delete rows with NaN
df = df.dropna()

#############################################################################
# Get Cumulative Stats from Runs

cumulativeDistanceStatsUrl, distanceParams = api.get_progress_summary_between_dates('2020-01-01', today, 'distance')
cumulativeElevationStatsUrl, elevationParams = api.get_progress_summary_between_dates('2020-01-01', today, 'elevationGain')

distance = garmin.connectapi(cumulativeDistanceStatsUrl, params=distanceParams)
elevation = garmin.connectapi(cumulativeElevationStatsUrl, params=elevationParams)

# Cumulative Distance
cumulativeRunningDistanceInCM = distance[0]['stats']['running']['distance']['sum']
cumulativeRunningDistanceInMiles = cumulativeRunningDistanceInCM*6.2137e-6

# Cumulative Elevation
cumulativeRunningElevationInCM = elevation[0]['stats']['running']['elevationGain']['sum']
cumulativeRunningElevationInMiles = cumulativeRunningElevationInCM*6.2137e-6

cumulativeDf = [{"Distance": cumulativeRunningDistanceInMiles, "Elevation": cumulativeRunningElevationInMiles}]
cumulativeDf = pd.DataFrame(cumulativeDf)
#############################################################################
# Google Sheets
gc = gsheets.authenticate()

# # Select sheet
sheet, gs = gsheets.selectSheet(gc, os.getenv('SHEETKEY'), 'Steps')
# # Append yesterday's steps to the sheet
gsheets.appendSheet(sheet, df, gs)

sheet, gs = gsheets.selectSheet(gc, os.getenv('SHEETKEY'), 'Cumulative')
# Add cumulative stats to the sheet
gsheets.setSheet(sheet, cumulativeDf)