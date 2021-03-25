import time
import datetime as dt
import tkinter
from tkinter import messagebox
from tkinter import simpledialog
import winsound


time_now = dt.datetime.now()
time_pom = 25*60
time_delta = dt.timedelta(0, time_pom)
time_future = time_now + time_delta
break_time = 5*60 
time_done = time_now + dt.timedelta(0, time_pom+break_time)

root = tkinter.Tk()
root.withdraw()
messagebox.showinfo("Pomodore Timer Started!", "The time is now " + time_now.strftime("%H:  %M") + "\n25 mins starting now")

hosts_path = r'C:\Windows\System32\drivers\etc'
redirect = "127.0.0.1"
website_list = ["crunchyroll.com", "www.crunchyroll.com", "www.netflix.com", "netflix.com"]

total_pomodoros = 0

timenow = time_now.strftime("%H:%M") 


def add_website(filepath):
    with open(filepath+"/hosts","r+") as dummy_file:
        content = dummy_file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                dummy_file.write(redirect+"\t"+website+"\n")

def remove_website(filepath):
    with open(filepath+"/hosts", "r+") as file:
        content = file.readlines()
        file.seek(0)
        for lines in content:
            if not any(website in lines for website in website_list):
                file.write(lines)
        file.truncate()

print(f"Bug check 0: \ntime_now: {time_now}\ntime_future: {time_future}")

while True:
    if time_now < time_future:
        add_website(hosts_path)
        print('Pomodore')

    elif time_future <= time_now <= time_done:
        print('You are in your break')
        messagebox.showinfo("Break Started!", "\nIt is now "+ time_now)
        remove_website(hosts_path)

    else:
        print('You are finished') 
        print('\a')
        for i in range(10):
            winsound.Beep((i+100), 500)   
        remove_website(hosts_path)  

        user_ans = messagebox.askyesno("Pomodore clock finished!", "Would you like to start another one?")

        total_pomodoros += 1

        if user_ans == True:
            time_now = dt.datetime.now()
            time_future = time_now + dt.timedelta(0, time_pom)
            time_done = time_now + dt.timedelta(0, time_pom+break_time)
            continue

        elif user_ans == False:
            print(f'Pomodoro timer complete! \nYou have completed {total_pomodoros} pomodoros today.')
            messagebox.showinfo("Pomodoro Finished!", "\nIt is now "+timenow+"\nYou completed "+str(total_pomodoros)+" pomodoros today!")
            break
    print('sleeping')
    time.sleep(20)
    time_now = dt.datetime.now()


print('\n\nMade it to the end!\n\n')
    

