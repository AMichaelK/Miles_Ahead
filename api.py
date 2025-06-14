import logging

logger = logging.getLogger(__name__)

class GarminAPI:

    def __init__(self, displayName: str = None):
        self.display_name = displayName

    garmin_connect_daily_summary_url = ("/usersummary-service/usersummary/daily")
    garmin_connect_metrics_url = ("/metrics-service/metrics/maxmet/daily")
    garmin_connect_daily_stats_steps_url = ("/usersummary-service/stats/steps/daily")
    garmin_connect_personal_record_url = ("/personalrecord-service/personalrecord/prs")
    garmin_connect_earned_badges_url = "/badge-service/badge/earned"
    garmin_connect_adhoc_challenges_url = ("/adhocchallenge-service/adHocChallenge/historical")
    garmin_connect_adhoc_challenge_url = ("/adhocchallenge-service/adHocChallenge/")
    garmin_connect_badge_challenges_url = ("/badgechallenge-service/badgeChallenge/completed")
    garmin_connect_available_badge_challenges_url = ("/badgechallenge-service/badgeChallenge/available")
    garmin_connect_inprogress_virtual_challenges_url = ("/badgechallenge-service/virtualChallenge/inProgress")
    garmin_connect_daily_sleep_url = ("/wellness-service/wellness/dailySleepData")
    garmin_connect_daily_stress_url = ("/wellness-service/wellness/dailyStress")
    garmin_connect_hill_score_url = ("/metrics-service/metrics/hillscore")

    garmin_connect_daily_body_battery_url = ("/wellness-service/wellness/bodyBattery/reports/daily")

    garmin_connect_endurance_score_url = ("/metrics-service/metrics/endurancescore")

    garmin_connect_rhr_url = "/userstats-service/wellness/daily"

    garmin_connect_hrv_url = "/hrv-service/hrv"

    garmin_connect_training_readiness_url = ("/metrics-service/metrics/trainingreadiness")

    garmin_connect_race_predictor_url = ("/metrics-service/metrics/racepredictions")
    garmin_connect_training_status_url = ("/metrics-service/metrics/trainingstatus/aggregated")
    garmin_connect_user_summary_chart = ("/wellness-service/wellness/dailySummaryChart")
    garmin_connect_floors_chart_daily_url = ("/wellness-service/wellness/floorsChartData/daily")
    garmin_connect_heartrates_daily_url = ("/wellness-service/wellness/dailyHeartRate")
    garmin_connect_daily_respiration_url = ("/wellness-service/wellness/daily/respiration")
    garmin_connect_daily_spo2_url = ("/wellness-service/wellness/daily/spo2")
    garmin_connect_daily_intensity_minutes = ("/wellness-service/wellness/daily/im")
    garmin_connect_activities = ("/activitylist-service/activities/search/activities")
    garmin_connect_activities_baseurl = ("/activitylist-service/activities/")
    garmin_connect_activity = "/activity-service/activity"
    garmin_connect_activity_types = ("/activity-service/activity/activityTypes")
    garmin_connect_activity_fordate = ("/mobile-gateway/heartRate/forDate")
    garmin_connect_fitnessstats = "/fitnessstats-service/activity"
    garmin_connect_fitnessage = "/fitnessage-service/fitnessage"

    garmin_connect_fit_download = "/download-service/files/activity"
    garmin_connect_tcx_download = ("/download-service/export/tcx/activity")
    garmin_connect_gpx_download = ("/download-service/export/gpx/activity")
    garmin_connect_kml_download = ("/download-service/export/kml/activity")
    garmin_connect_csv_download = ("/download-service/export/csv/activity")
    garmin_graphql_endpoint = "graphql-gateway/graphql"

    def get_display_name(self, garth):
        self.display_name = garth.client.profile['displayName']

#     def get_steps_data(self, cdate):
#         """Fetch available steps data 'cDate' format 'YYYY-MM-DD'."""

#         url = f"{self.garmin_connect_user_summary_chart}/{self.display_name}"
#         params = {"date": str(cdate)}
#         logger.debug("Requesting steps data")

#         return (url, params=params)

#     def get_floors(self, cdate):
#         """Fetch available floors data 'cDate' format 'YYYY-MM-DD'."""

#         url = f"{self.garmin_connect_floors_chart_daily_url}/{cdate}"
#         logger.debug("Requesting floors data")

#         return (url)

    def get_daily_steps(self, start, end):
        """Fetch available steps data 'start' and 'end' format 'YYYY-MM-DD'."""

        url = f"{self.garmin_connect_daily_stats_steps_url}/{start}/{end}"
        logger.debug("Requesting daily steps data")

        return (url)

#     def get_heart_rates(self, cdate):
#         """Fetch available heart rates data 'cDate' format 'YYYY-MM-DD'."""

#         url = f"{self.garmin_connect_heartrates_daily_url}/{self.display_name}"
#         params = {"date": str(cdate)}
#         logger.debug("Requesting heart rates")

#         return (url, params=params)

#     def get_body_battery(
#         self, startdate: str, enddate=None
#     ) -> List[Dict[str, Any]]:
#         """
#         Return body battery values by day for 'startdate' format
#         'YYYY-MM-DD' through enddate 'YYYY-MM-DD'
#         """

#         if enddate is None:
#             enddate = startdate
#         url = self.garmin_connect_daily_body_battery_url
#         params = {"startDate": str(startdate), "endDate": str(enddate)}
#         logger.debug("Requesting body battery data")

#         return (url, params=params)

#     def get_intensity_minutes_data(self, cdate: str) -> Dict[str, Any]:
#         """Return available Intensity Minutes data 'cdate' format 'YYYY-MM-DD'."""

#         url = f"{self.garmin_connect_daily_intensity_minutes}/{cdate}"
#         logger.debug("Requesting Intensity Minutes data")

#         return (url)

#     def get_personal_record(self) -> Dict[str, Any]:
#         """Return personal records for current user."""

#         url = f"{self.garmin_connect_personal_record_url}/{self.display_name}"
#         logger.debug("Requesting personal records for user")

#         return (url)

#     def get_earned_badges(self) -> Dict[str, Any]:
#         """Return earned badges for current user."""

#         url = self.garmin_connect_earned_badges_url
#         logger.debug("Requesting earned badges for user")

#         return (url)

#     def get_adhoc_challenges(self, start, limit) -> Dict[str, Any]:
#         """Return adhoc challenges for current user."""

#         url = self.garmin_connect_adhoc_challenges_url
#         params = {"start": str(start), "limit": str(limit)}
#         logger.debug("Requesting adhoc challenges for user")

#         return (url, params=params)

#     def get_badge_challenges(self, start, limit) -> Dict[str, Any]:
#         """Return badge challenges for current user."""

#         url = self.garmin_connect_badge_challenges_url
#         params = {"start": str(start), "limit": str(limit)}
#         logger.debug("Requesting badge challenges for user")

#         return (url, params=params)

#     def get_available_badge_challenges(self, start, limit) -> Dict[str, Any]:
#         """Return available badge challenges."""

#         url = self.garmin_connect_available_badge_challenges_url
#         params = {"start": str(start), "limit": str(limit)}
#         logger.debug("Requesting available badge challenges")

#         return (url, params=params)

#     def get_inprogress_virtual_challenges(
#         self, start, limit
#     ) -> Dict[str, Any]:
#         """Return in-progress virtual challenges for current user."""

#         url = self.garmin_connect_inprogress_virtual_challenges_url
#         params = {"start": str(start), "limit": str(limit)}
#         logger.debug("Requesting in-progress virtual challenges for user")

#         return (url, params=params)

#     def get_sleep_data(self, cdate: str) -> Dict[str, Any]:
#         """Return sleep data for current user."""

#         url = f"{self.garmin_connect_daily_sleep_url}/{self.display_name}"
#         params = {"date": str(cdate), "nonSleepBufferMinutes": 60}
#         logger.debug("Requesting sleep data")

#         return (url, params=params)

#     def get_rhr_day(self, cdate: str) -> Dict[str, Any]:
#         """Return resting heartrate data for current user."""

#         url = f"{self.garmin_connect_rhr_url}/{self.display_name}"
#         params = {
#             "fromDate": str(cdate),
#             "untilDate": str(cdate),
#             "metricId": 60,
#         }
#         logger.debug("Requesting resting heartrate data")

#         return (url, params=params)

#     def get_hrv_data(self, cdate: str) -> Dict[str, Any]:
#         """Return Heart Rate Variability (hrv) data for current user."""

#         url = f"{self.garmin_connect_hrv_url}/{cdate}"
#         logger.debug("Requesting Heart Rate Variability (hrv) data")

#         return (url)

#     def get_training_readiness(self, cdate: str) -> Dict[str, Any]:
#         """Return training readiness data for current user."""

#         url = f"{self.garmin_connect_training_readiness_url}/{cdate}"
#         logger.debug("Requesting training readiness data")

#         return (url)

#     def get_endurance_score(self, startdate: str, enddate=None):
#         """
#         Return endurance score by day for 'startdate' format 'YYYY-MM-DD'
#         through enddate 'YYYY-MM-DD'.
#         Using a single day returns the precise values for that day.
#         Using a range returns the aggregated weekly values for that week.
#         """

#         if enddate is None:
#             url = self.garmin_connect_endurance_score_url
#             params = {"calendarDate": str(startdate)}
#             logger.debug("Requesting endurance score data for a single day")

#             return (url, params=params)
#         else:
#             url = f"{self.garmin_connect_endurance_score_url}/stats"
#             params = {
#                 "startDate": str(startdate),
#                 "endDate": str(enddate),
#                 "aggregation": "weekly",
#             }
#             logger.debug("Requesting endurance score data for a range of days")

#             return (url, params=params)

    def get_race_predictions(self, startdate=None, enddate=None, _type=None):
        """
        Return race predictions for the 5k, 10k, half marathon and marathon.
        Accepts either 0 parameters or all three:
        If all parameters are empty, returns the race predictions for the current date
        Or returns the race predictions for each day or month in the range provided

        Keyword Arguments:
        'startdate' the date of the earliest race predictions
        Cannot be more than one year before 'enddate'
        'enddate' the date of the last race predictions
        '_type' either 'daily' (the predictions for each day in the range) or
        'monthly' (the aggregated monthly prediction for each month in the range)
        """

        valid = {"daily", "monthly", None}
        if _type not in valid:
            raise ValueError("results: _type must be one of %r." % valid)

        if _type is None and startdate is None and enddate is None:
            url = (
                self.garmin_connect_race_predictor_url
                + f"/latest/{self.display_name}"
            )
            return (url)

        elif (
            _type is not None and startdate is not None and enddate is not None
        ):
            url = (
                self.garmin_connect_race_predictor_url
                + f"/{_type}/{self.display_name}"
            )
            params = {
                "fromCalendarDate": str(startdate),
                "toCalendarDate": str(enddate),
            }
            return (url, params)

        else:
            raise ValueError(
                "You must either provide all parameters or no parameters"
            )

#     def get_training_status(self, cdate: str) -> Dict[str, Any]:
#         """Return training status data for current user."""

#         url = f"{self.garmin_connect_training_status_url}/{cdate}"
#         logger.debug("Requesting training status data")

#         return (url)

#     def get_hill_score(self, startdate: str, enddate=None):
#         """
#         Return hill score by day from 'startdate' format 'YYYY-MM-DD'
#         to enddate 'YYYY-MM-DD'
#         """

#         if enddate is None:
#             url = self.garmin_connect_hill_score_url
#             params = {"calendarDate": str(startdate)}
#             logger.debug("Requesting hill score data for a single day")

#             return (url, params=params)

#         else:
#             url = f"{self.garmin_connect_hill_score_url}/stats"
#             params = {
#                 "startDate": str(startdate),
#                 "endDate": str(enddate),
#                 "aggregation": "daily",
#             }
#             logger.debug("Requesting hill score data for a range of days")

#             return (url, params=params)

#     def get_activities(self, start: int = 0, limit: int = 20, activitytype: Optional[str] = None):
#         """
#         Return available activities.
#         :param start: Starting activity offset, where 0 means the most recent activity
#         :param limit: Number of activities to return
#         :param activitytype: (Optional) Filter activities by type
#         :return: List of activities from Garmin
#         """

#         url = self.garmin_connect_activities
#         params = {"start": str(start), "limit": str(limit)}
#         if activitytype:
#             params["activityType"] = str(activitytype)

#         logger.debug("Requesting activities")

#         return (url, params=params)

#     def get_activities_fordate(self, fordate: str):
#         """Return available activities for date."""

#         url = f"{self.garmin_connect_activity_fordate}/{fordate}"
#         logger.debug(f"Requesting activities for date {fordate}")

#         return (url)

#     def get_last_activity(self):
#         """Return last activity."""

#         activities = self.get_activities(0, 1)
#         if activities:
#             return activities[-1]

#         return None

#     def get_activities_by_date(
#         self, startdate, enddate=None, activitytype=None, sortorder=None
#     ):
#         """
#         Fetch available activities between specific dates
#         :param startdate: String in the format YYYY-MM-DD
#         :param enddate: (Optional) String in the format YYYY-MM-DD
#         :param activitytype: (Optional) Type of activity you are searching
#                              Possible values are [cycling, running, swimming,
#                              multi_sport, fitness_equipment, hiking, walking, other]
#         :param sortorder: (Optional) sorting direction. By default, Garmin uses descending order by startLocal field.
#                           Use "asc" to get activities from oldest to newest.
#         :return: list of JSON activities
#         """

#         activities = []
#         start = 0
#         limit = 20
#         # mimicking the behavior of the web interface that fetches
#         # 20 activities at a time
#         # and automatically loads more on scroll
#         url = self.garmin_connect_activities
#         params = {
#             "startDate": str(startdate),
#             "start": str(start),
#             "limit": str(limit),
#         }
#         if enddate:
#             params["endDate"] = str(enddate)
#         if activitytype:
#             params["activityType"] = str(activitytype)
#         if sortorder:
#             params["sortOrder"] = str(sortorder)

#         logger.debug(
#             f"Requesting activities by date from {startdate} to {enddate}"
#         )
#         while True:
#             params["start"] = str(start)
#             logger.debug(f"Requesting activities {start} to {start+limit}")
#             act = (url, params=params)
#             if act:
#                 activities.extend(act)
#                 start = start + limit
#             else:
#                 break

#         return activities

    def get_progress_summary_between_dates(
        self, startdate, enddate, metric, groupbyactivities=True
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

        url = self.garmin_connect_fitnessstats
        params = {
            "startDate": str(startdate),
            "endDate": str(enddate),
            "aggregation": "lifetime",
            "groupByParentActivityType": str(groupbyactivities),
            "metric": str(metric),
        }

        logger.debug(
            f"Requesting fitnessstats by date from {startdate} to {enddate}"
        )
        return (url, params)

#     def get_activity_types(self):
#         url = self.garmin_connect_activity_types
#         logger.debug("Requesting activity types")
#         return (url)

#     def get_gear(self, userProfileNumber):
#         """Return all user gear."""
#         url = f"{self.garmin_connect_gear}?userProfilePk={userProfileNumber}"
#         logger.debug("Requesting gear for user %s", userProfileNumber)

#         return (url)

#     def get_gear_stats(self, gearUUID):
#         url = f"{self.garmin_connect_gear_baseurl}stats/{gearUUID}"
#         logger.debug("Requesting gear stats for gearUUID %s", gearUUID)
#         return (url)

#     def get_gear_defaults(self, userProfileNumber):
#         url = (
#             f"{self.garmin_connect_gear_baseurl}user/"
#             f"{userProfileNumber}/activityTypes"
#         )
#         logger.debug("Requesting gear for user %s", userProfileNumber)
#         return (url)