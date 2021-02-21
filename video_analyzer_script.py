# Download the helper library from https://www.twilio.com/docs/python/install
import sys
import os
import time
import _thread as thread
import threading
from twilio.rest import Client
from datetime import date, timedelta
from dateutil.parser import parse
import multiprocessing 
from multiprocessing import Pool, cpu_count

def tern_init(some_arg, num):
    try:
        return some_arg[num]
    except:
        return "None"

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True
    except ValueError:
        return False

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

def get_date_fr(arg_date, arg_date_2):
    tmp_date={
        "date_1": "",
        "date_2": ""
    }
    if not is_date(arg_date):
        if("day" in arg_date): # today's usage
            print("I'm here day")
            tmp_date["date_1"]=(date.today() - timedelta(days=1)).strftime("%d-%m-%Y")
        if("week" in arg_date): # current week usage
            print("I'm here week")
            tmp_date["date_1"]=(date.today() - timedelta(days=date.today().weekday())).strftime("%d-%m-%Y")
            tmp_date["date_2"]=(date.today() - timedelta(days=1)).strftime("%d-%m-%Y")
        if("month" in arg_date): # current month usage 
            print("I'm here month")
            tmp_date["date_1"]=date.today().replace(day=1).strftime("%d-%m-%Y")
            tmp_date["date_2"]=(date.today() - timedelta(days=1)).strftime("%d-%m-%Y")
    else:
        tmp_date["date_1"]=arg_date
        tmp_date["date_2"]=arg_date_2
    return tmp_date

def get_participant_details(room_sid, participant_sid): #, participant_count, room_count
    twilio = Client(account_sid, auth_token)
    p=twilio.video.rooms(room_sid).participants.get(participant_sid).fetch()
    print(p.fetch().room_sid,",", p.fetch().sid,",",p.fetch().duration,",",p.fetch().start_time,",",p.fetch().end_time)
    return p.fetch().duration

account_sid=sys.argv[1] 
auth_token=sys.argv[2] 
date_1=tern_init(sys.argv,3)
date_2=tern_init(sys.argv,4)

def main():
    client = Client(account_sid, auth_token)
    start = time.time()
    date_fr=get_date_fr(date_1, date_2)

    print("date_1:",date_fr["date_1"])
    print("date_2:",date_fr["date_2"])

    total_video_room=[]
    total_participants=[]

    print("Particpant Count,Room Count,Room SID,Participant SID,Duration,Start Time,End Time")
    for v in client.video.rooms.list(status='completed', date_created_after=parse(date_fr["date_1"]) if is_date(date_fr["date_1"]) else None, date_created_before=parse(date_fr["date_2"]) if is_date(date_fr["date_2"]) else None):
        total_video_room.append(v.sid)

    for room_sid in total_video_room:
        participants = client.video.rooms(room_sid).participants
        for p in participants.list(status='disconnected'):
            total_participants.append((room_sid, p.sid))
    
    # NOTE: Current performance: 2N/X where N is the number of video rooms and X is the number of thread in the machine (around 0.7 seconds per participants w/o print, 1.2 seconds w print)
    print(f'running duration for {len(total_participants)} of participants')
    print(f'starting computations on {cpu_count()} cores')
    with Pool() as pool:
        try:
            res = pool.starmap(get_participant_details, total_participants)
            print(res)
            print("Total minutes: {:.2f}".format(sum(res)/60))
        except Exception as e:
            print ("Error: unable to start thread,", e)

    #End Lapse Time
    end = time.time()
    print("Time taken: {:.2f} seconds".format(end - start))

if __name__ == '__main__':
    main()
