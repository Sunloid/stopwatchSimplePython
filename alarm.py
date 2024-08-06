import time 
from win10toast import ToastNotifier

toaster = ToastNotifier()

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

title = "Alarm"
message = "Time up!!"

def alarm(seconds):
    time_elapsed = 0 
    print(CLEAR)

    while time_elapsed < seconds:    
        time.sleep(1)
        time_elapsed+=1 
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 
        seconds_left = time_left % 60

        print(f"{minutes_left:02d}:{seconds_left:02d}")
    toaster.show_toast(title, message )


minutesTotal = int(input("How many minutes to wait: "))
secondsTotal = int(input("How many seconds to wait: "))
Total = minutesTotal * 60 + secondsTotal
alarm(Total)