# Twilio Video Minutes Tabulation Script
This script takes in a Account SID and Auth Token provided by Twilio and runs through the whole Video Logs in your Account. This script is not efficient in anyway but does help consolidate all the seconds and consolidate them into an estimated minutes.

## Requirement
Python3 - https://www.python.org/downloads/
Twilio Python Helper Library - pip install twilio

## Command (Windows)
```bash
# Running the Python Script
$ python video_analyzer_script.py [ACCOUNT_SID] [AUTH_TOKEN]

# Running the Python Script export to csv
$ python video_analyzer_script.py [ACCOUNT_SID] [AUTH_TOKEN] > video_all.csv
```

## Performance
On average 1 entry takes 2 seconds, so that's 2N seconds given N number of particiapnts.
Example - 3,000 particpants will 6,000 seconds (equivalent to 100 minutes)
