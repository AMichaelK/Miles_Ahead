# Miles Ahead

Welcome!

Miles Ahead is Python-based project that pulls fitness stats from Garmin and syncs them in a Google Sheet for visualization in Grafana!

Nightly updates are automated via GitHub Actions which build and run a Docker container to aggregate fresh data.

## Features
* Retrieves Garmin activity data using [Garth](https://github.com/matin/garth) and [Python-GarminConnect](https://github.com/cyberjunky/python-garminconnect/tree/master).
* Syncs data to Google Sheets
* Visualized via Grafana dashboards
* Automated daily updates using GitHub Actions and Docker

## Quick Start
Please refer to `reference.py` for an overview of core functionality and usage.