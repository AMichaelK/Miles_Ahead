import os
from auth import GarminAuth
from api import GarminAPI
from datetime import date, timedelta

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

# Get steps from yesterday
# steps = garmin.connectapi("/usersummary-service/stats/steps/daily/2025-06-03/2025-06-03")
url = api.get_daily_steps(yesterday, yesterday)
steps = garmin.connectapi(url)

for i in steps:
    print(i)

# Get steps from past 28 days

url = api.get_daily_steps(TwentyEightDaysAgo, yesterday)
steps = garmin.connectapi(url)

for i in steps:
    print(i)