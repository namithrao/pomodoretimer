import time
import datetime as dt
import tkinter
from tkinter import messagebox
import winsound


time_now = dt.datetime.now()
time_pom = 25*60
time_delta = dt.timedelta(0, time_pom)
time_future = time_now + time_delta
break_time = 5*60 
time_done = time_now + dt.timedelta(0, time_pom+break_time)

window = tkinter.Tk()
window.withdraw()
messagebox.showinfo("Pomodore Timer Started!", "The time is now " + time_now.strftime("%H:  %M") + "\n25 mins starting now")

total_pomodoros = 0
breaks = 0

while True:
    if time_now < time_future:
        print('Pomodore')

    elif time_future <= time_now <= time_done:
        print('You are in your break')

        if breaks == 0:
            print('if break')
            for i in range (5):
                winsound.Beep((i+100), 700)
            print('Break Time')
            breaks += 1
    else:
        print('You are finished') 

        breaks = 0
        for i in range(10):
            winsound.Beep((i+100), 500)     

        user_ans = messagebox.askyesno("Pomodore clock finished!", "Would you like to start another one?")

        total_pomodoros += 1

        if user_ans == True:
            time_now = dt.datetime.now()
            time_future = time_now + dt.timedelta(0, time_pom)
            time_done = time_now + dt.timedelta(0, time_pom+break_time)
            continue

        elif user_ans == False:
            messagebox.showinfo("Pomodore timer finished!", "You have completed " + str(total_pomodoros) + "pomodoros today!")
            break
print('sleeping')
time.sleep(20)
time_now = dt.datetime.now()
timenow = time_now.strftime("%H:%M") 

