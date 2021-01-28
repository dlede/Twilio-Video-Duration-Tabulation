# Download the helper library from https://www.twilio.com/docs/python/install
import sys
from twilio.rest import Client
import time

start = time.time()

account_sid=sys.argv[1] 
auth_token=sys.argv[2] 
client = Client(account_sid, auth_token)

total_units=0
room_count=0
participant_count=0

print("Particpant Count,Room Count,Room SID,Participant SID,Duration,Start Time,End Time")
for v in client.video.rooms.list(status='completed'):
    room_count=room_count+1
    participants = client.video.rooms(v.sid).participants
    for p in participants.list(status='disconnected'):
        participant_count=participant_count+1
        print(participant_count,",",room_count,",",p.fetch().room_sid,",", p.fetch().sid,",",p.fetch().duration,",",p.fetch().start_time,",",p.fetch().end_time)
        total_units=total_units+p.fetch().duration

print("Total minutes:","{:.2f}".format(total_units/60))

#End Lapse Time
end = time.time()
print("Time taken:",end - start)