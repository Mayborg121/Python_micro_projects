from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()

st.title("ShutDown App")
st.geometry("300x270")
st.config(bg="cyan")

r_button = Button(st,text="Restart",font=("Time New Roman",15,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=105,y=30,height=30,width=90)

rt_button = Button(st,text="Restart Time:",font=("Time New Roman",10,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=105,y=90,height=30,width=90)

lo_button = Button(st,text="Log Out",font=("Time New Roman",15,"bold"),relief=RAISED,cursor="plus",command=logout)
lo_button.place(x=105,y=150,height=30,width=90)

st_button = Button(st,text="ShutDown",font=("Time New Roman",13,"bold"),relief=RAISED,cursor="plus",command=shutdown)
st_button.place(x=105,y=210,height=30,width=90)



st.mainloop()