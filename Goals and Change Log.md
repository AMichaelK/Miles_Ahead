<h1> Goals </h1>

- [x] Steps only
    - [x] Get daily steps
    - [x] Create Grafana chart
    - [x] Get previous month steps
- [x] Google Sheets
    - [x] Authenticate
    - [x] Update sheets
    - [x] Append daily step data
- [x] Github Actions
    - [x] Run an example file
    - [x] Run an example file with parameters
    - [x] Run a docker container from Docker Hub
    - [x] Run a docker container (with env variables) from Docker Hub
    - [x] Set up keys/creds
        - [x] Can I programmatically save env variables? Or is it ephemeral?
              No. But you can save it in steps output or save it using github cli "gh"
        - [x] Authenticate w/ Garmin while running via Github Actions -> Docker Run
        - [x] Authenticate w/ Google Sheetsvia Github Actions -> Docker Run
    - [x] Set up daily runs
- [ ] Create pipeline for getting steps to grafana chart
    - [x] Dockerize container
    - [x] Set up credentials to run from Docker to Gsheets
    - [x] CICD + Credentials
        - [x] Github actions
        - [ ] Azure DevOps
    - [x] Push data to Grafana
- [ ] Grafana
    - [x] Set up graph for daily steps
        - [x] Show actual, target
    - [ ] More metrics
        - [x] Race Predictions
        - [x] Total miles & elevation gained while running since x date
            - [ ] Compare mileage to large cities in the world?
        - [ ] Total stairs (per month from start date? but just show YTD?)
            - [ ] Compare to world's largest mountains
        - [ ] Calories burned
        - [ ] Intensity Minutes / Goal   
    