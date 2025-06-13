import os
from auth import GarminAuth
from api import GarminAPI
from datetime import date, timedelta
from dotenv import load_dotenv
import pandas as pd
from gsheets import GSheets
from comparisonVariables import Comparisons

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
cumulativeRunningElevationInMiles = cumulativeRunningElevationInCM/30.48

# Setting up Distance DataFrame
DISTANCE_TUPLE = Comparisons.DISTANCE_TUPLE
# print(json.dumps(Comparisons.DISTANCE_DICT, indent="\t"))
distanceDf = pd.DataFrame(DISTANCE_TUPLE, columns=['Name', 'Distance'])
new_row = {'Name': 'Me', 'Distance': cumulativeRunningDistanceInMiles}
distanceDf.loc[len(distanceDf)] = new_row

print(distanceDf)

# Setting up Elevation DataFrame
ELEVATION_TUPLE = Comparisons.HEIGHTS_TUPLE
elevationDf = pd.DataFrame(ELEVATION_TUPLE, columns=['Name', 'Elevation'])
new_row = {'Name': 'Me', 'Elevation': cumulativeRunningElevationInMiles}
elevationDf.loc[len(elevationDf)] = new_row
print(elevationDf)
#############################################################################
# Google Sheets
gc = gsheets.authenticate()

# # Select sheet
sheet, gs = gsheets.selectSheet(gc, os.getenv('SHEETKEY'), 'Steps')
# # Append yesterday's steps to the sheet
gsheets.appendSheet(sheet, df, gs)

sheet, gs = gsheets.selectSheet(gc, os.getenv('SHEETKEY'), 'CumulativeDistance')
# Add cumulative stats to the sheet
gsheets.setSheet(sheet, distanceDf)

sheet, gs = gsheets.selectSheet(gc, os.getenv('SHEETKEY'), 'CumulativeElevation')
gsheets.setSheet(sheet, elevationDf)