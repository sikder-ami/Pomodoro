from math import floor
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
check=''
reset=0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global check
    global reset
    reps=0
    check=''
    reset=1
    start.config(state='active')

def work_done():
    window.deiconify()          # restore if minimized
    # window.lift()               # bring to front
    window.attributes('-topmost', True)

    # turn off always-on-top after appearing
    window.after(10, lambda: window.attributes('-topmost', False))

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global check
    global reset

    start.config(state='disabled')
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    reset=0

    if reps%2==0:
        count_down(work_sec)
        timer.config(text='WORK',fg=RED,bg=GREEN)
        check += '🗹'

    elif reps%2==1 and not reps%7==0:
        count_down(short_break_sec)
        timer.config(text='Break', fg=YELLOW, bg=GREEN)
        checkmark.config(text=check)
        work_done()

    else:
        count_down(long_break_sec)
        timer.config(text='Break', fg=PINK, bg=GREEN)
        checkmark.config(text=check)
        work_done()

    reps=reps+1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes=math.floor(count/60)
    seconds=math.floor(count%60)

    canvas.itemconfig(timer_text, text=f'{minutes:02}:{seconds:02}')
    if reset==1:
        canvas.itemconfig(timer_text, text='00:00')
        timer.config(text='Timer', fg=RED, bg=GREEN)
        checkmark.config(text=check)

    else:
        if count > 0:
            window.after(1000, count_down,count-1)
        elif count == 0 :
            start_timer()




# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title('Pomodoro')
window.configure(padx=100, pady=50, bg=GREEN)

timer=Label(window, text="Timer", font=(FONT_NAME,40,'bold'),bg=GREEN,fg=RED)
timer.grid(row=0, column=1)

canvas=Canvas(window,width=200,height=224, bg=GREEN,highlightthickness=0 )
tmt=PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tmt)
timer_text=canvas.create_text(100,130, text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)

start=Button(text='Start',font=(FONT_NAME,12),highlightthickness=0,command=start_timer)
start.grid(row=2,column=1)
start.grid(row=3, column=0)

Reset=Button(text='Reset',font=(FONT_NAME,12),highlightthickness=0,command=reset_timer)
Reset.grid(row=3, column=2)

checkmark=Label(font=(FONT_NAME,25),fg=RED,bg=GREEN)
checkmark.grid(row=4,column=1)


window.mainloop()