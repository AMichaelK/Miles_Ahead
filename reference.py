# %%
import garth
import os
from dotenv import load_dotenv
import datetime
import pandas as pd

# Refresh dotenv
load_dotenv(override=True)
#####################################################################
# Part1 :Login
# Try to resume Garth from file, if not, login
# if garth.resume("~/.garth"):
#     pass
# else:
garth.login(os.getenv('EMAIL'), os.getenv('PASS'))

# %%
print(dir(garth))
print((garth.client.profile['displayName']))

displayName=(garth.client.profile['displayName'])


# %%
#####################################################################
# Part 2: Race Predictions
# RACE PREDICTIONS
garmin_connect_race_predictor_url = ("/metrics-service/metrics/racepredictions")

# current
currentUrl=f"{garmin_connect_race_predictor_url}/latest/{displayName}" 
race_predictions = garth.connectapi(currentUrl)
print(race_predictions)

# %%
# Get race predictions

params = {
     "fromCalendarDate": str('2025-04-01'),
     "toCalendarDate": str('2025-06-01')
}
# print(str(startdate))
monthlyUrl=f"{garmin_connect_race_predictor_url}/monthly/{displayName}"
monthly_race_predictions = garth.connectapi(monthlyUrl,params = params)
print(monthly_race_predictions)

# dailyUrl=f"{garmin_connect_race_predictor_url}/daily/{displayName}"
# daily_race_predictions = garth.connectapi(dailyUrl,params = params)
# print(daily_race_predictions)

# %%
# Now we grab that and stick it in pandas
df = pd.DataFrame(monthly_race_predictions)
df = df.dropna()
predictDf = df.drop(df.columns[0], axis=1)
print(predictDf)

# %%
# Convert seconds to HMS
def format_to_hours_minutes_seconds(x):
    td = datetime.timedelta(seconds=x)
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return(f"{hours:02}:{minutes:02}:{seconds:02}")

for col in predictDf.columns[3:]:
    predictDf[col] = predictDf[col].apply(format_to_hours_minutes_seconds)

print(predictDf)
# %%
#####################################################################
# Part 3: Daily Steps
# STEPS
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
#####################################################################
# Part 4: Daily Steps
# STEPS

garmin_connect_fitnessstats = "/fitnessstats-service/activity"

startdate='2020-01-01'
enddate='2025-06-01'
metric='distance' # could also be "elevationGain", "duration", "distance", "movingDuration"

progressStats = garth.connectapi(garmin_connect_fitnessstats, params = {
        "startDate": str(startdate),
        "endDate": str(enddate),
        "aggregation": "lifetime",
        "groupByParentActivityType": 'True',
        "metric": str(metric),
})



def get_progress_summary_between_dates(
    self, startdate, enddate, metric="distance", groupbyactivities=True
):
    """
    Fetch progress summary data between specific dates
    :param startdate: String in the format YYYY-MM-DD
    :param enddate: String in the format YYYY-MM-DD
    :param metric: metric to be calculated in the summary:
        "elevationGain", "duration", "distance", "movingDuration"
    :param groupbyactivities: group the summary by activity type
    :return: list of JSON activities with their aggregated progress summary
    """

    progressUrl = self.garmin_connect_fitnessstats
    params = {
        "startDate": str(startdate),
        "endDate": str(enddate),
        "aggregation": "lifetime",
        "groupByParentActivityType": str(groupbyactivities),
        "metric": str(metric),
    }
    # return (url, params=params)

# %%
#####################################################################
# Part 5: Connect to GSheets
from google.oauth2.service_account import Credentials
import gspread
from dotenv import load_dotenv

load_dotenv(override=True)

scopes = ['https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive']


credentials = Credentials.from_service_account_file(os.getenv('SACREDS'), scopes=scopes)
gc = gspread.authorize(credentials)

# %%
#####################################################################
# Part 6: Stick Steps in GSheets
# Select Worksheet and Tab
gs = gc.open_by_key(os.getenv('SHEETKEY'))
sheet = gs.worksheet('Steps')

# %% 
# Append DataFrame and GSheets Tab
df_values = df.values.tolist()
gs.values_append('Steps', {'valueInputOption': 'RAW'}, {'values': df_values})

# %%
#####################################################################
# Part 7: Race Predictions in GSheets
# Select Race Predictions Tab
sheet = gs.worksheet('RacePredictions')

# %%
# Append Prediction DataFrame to GSheets
predictDf_values = predictDf.values.tolist()
gs.values_append('RacePredictions', {'valueInputOption': 'RAW'}, {'values': predictDf_values})

# %%
# Converting seconds to HMS
diff = datetime.timedelta(seconds=1473)
print(diff)

# %%
