from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time you want to set the alarm: HH:MM:SSam/pm\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[8:10].upper()
print("Setting Alarm...")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_period = now.strftime("%p")
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                print("Wake Up!")
                playsound("")
                break
