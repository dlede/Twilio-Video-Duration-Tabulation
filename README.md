# Disclaimer
This is not maintained by Twilio or represent Twilio in any way. 

# Twilio Video Minutes Tabulation Script
Currently there is no way to tabulate the duration of all the video you have used on [Twilio Video](https://www.twilio.com/docs/video/video-log-analyzer).
This script takes in a Account SID and Auth Token provided by Twilio and runs through the whole Video Logs in your Account. This script is not efficient in anyway but does help 
consolidate all the seconds and consolidate them into an estimated minutes.

It fetches all the (completed) Rooms in your account via [Room API](https://www.twilio.com/docs/video/api/rooms-resource?code-sample=code-retrieve-a-list-of-rooms-by-status&code-language=Python&code-sdk-version=6.x)

With all the Room SID, it fetches all the (disconnected) Participant via [Participant API](https://www.twilio.com/docs/video/api/participants?code-sample=code-retrieve-a-list-of-disconnected-participants-3&code-language=Python&code-sdk-version=default)

## Requirement
Python3 - https://www.python.org/downloads/

Twilio Python Helper Library - pip install twilio

## Command (Windows)
```bash
# Running the Python Script
$ python video_analyzer_script.py [ACCOUNT_SID] [AUTH_TOKEN]

# Running the Python Script export to csv
$ python video_analyzer_script.py [ACCOUNT_SID] [AUTH_TOKEN] > video_all.csv

# Running the Python Script specific to "today", "week", "month", specific date
$ python video_analyzer_script.py [ACCOUNT_SID] [AUTH_TOKEN] day
$ python video_analyzer_script.py [ACCOUNT_SID] [AUTH_TOKEN] week
$ python video_analyzer_script.py [ACCOUNT_SID] [AUTH_TOKEN] month
$ python video_analyzer_script.py [ACCOUNT_SID] [AUTH_TOKEN] [DATE_FROM] [DATE_TO]

# Running the Python Script and export to csv
$ python video_analyzer_script.py [ACCOUNT_SID] [AUTH_TOKEN] > video_all.csv
```

## Performance
Warning: This is not a very efficient way of tabulating Video Participants minutes and may or may not be 100% accurate. 
On average 1 entry takes 2 seconds, so that's 2N seconds given N number of particiapnts (individual participants have different duration in individual room).
Example - 3,000 particpants will 6,000 seconds (equivalent to 100 minutes) to run the script completely.
