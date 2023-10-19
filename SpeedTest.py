from tkinter import *
import speedtest


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6), 4))+"Mbps"
    up = str(round(sp.upload()/(10**6), 4))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title("NetSpeed")
sp.geometry("250x300")
sp.config(bg="Green")


lab = Label(sp, text="Internet Speed Test ",
            font=("Time New Roman", 15, "bold"), bg="Green", fg="white")
lab.place(x=32, y=35, height=30, width=195)

lab = Label(sp, text="Download Speed : ",
            font=("Time New Roman", 10, "bold"), bg="Green", fg="white")
lab.place(x=32, y=95, height=30, width=195)
lab_down = Label(sp, text="00",
                 font=("Time New Roman", 10, "bold"), bg="Green", fg="white")
lab_down.place(x=32, y=120, height=30, width=195)

lab = Label(sp, text="Upload Speed : ",
            font=("Time New Roman", 10, "bold"), bg="Green", fg="white")
lab.place(x=32, y=145, height=30, width=195)
lab_up = Label(sp, text="00",
               font=("Time New Roman", 10, "bold"), bg="Green", fg="white")
lab_up.place(x=32, y=170, height=30, width=195)

button = Button(sp, text="CHECK SPEED",
                font=("Time New Roman", 15, "bold"), bg="Maroon", fg="Cyan", relief=RAISED, command=speedcheck)
button.place(x=32, y=210, height=30, width=195)


sp.mainloop()
