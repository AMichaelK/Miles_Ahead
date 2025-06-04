import os
from auth import GarminAuth
from api import GarminAPI
from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)
yesterday = yesterday.isoformat()

garmin = GarminAuth(
    email = os.getenv("EMAIL"),
    password = os.getenv("PASS"),
    tokenstore = os.getenv("GARMINTOKENS")
)

garmin.login()

print(type(garmin))
print(dir(garmin))

# Get steps from yesterday
steps = garmin.connectapi(GarminAPI.get_daily_steps(date.today(), date.today()))
# Get steps from past 28 days