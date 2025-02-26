#Project : Count down Timer in Python
#Description: This is a countdown timer that takes input in seconds from the top and displays it in minute:second format

import time

def countdown_timer(seconds):
    while seconds > 0:
        mins,secs = divmod(seconds, 60) #minutes and seconds are calculated using divmod function
        time_format = '{:02d}:{:02d}'.format(mins, secs) #time format is formatted to 2 digits e.g 01:01
        print(time_format, end='\r')
        time.sleep(1) #delay of 1 second
        seconds -= 1
    print("00:00 \n Time's Up!")

#user input for timer
total_seconds = int(input("Enter the time in seconds for countdown: "))
countdown_timer(total_seconds)