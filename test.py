from tkinter import *
#import pymysql as mdb
#import pandas as pd
import time
from tkinter import messagebox
import datetime
import re
import os

class Booking:


    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.e_room = Entry(self.frame)
        self.e_facilities = Entry(self.frame)
        self.e_StaffID = Entry(self.frame)
        self.e_room.grid(row=0, column=1)
        self.e_facilities.grid(row=1, column=1)
        self.e_StaffID.grid(row=2, column=1)

        self.label_room = Label(self.frame, text="Room ID")
        self.label_facilities = Label(self.frame, text="Facilities")
        self.label_StaffID = Label(self.frame, text="Booked by")
        self.label_Participants = Label(self.frame, text="Participants")
        self.label_startTime = Label(self.frame, text="Start Time")
        self.label_endTime = Label(self.frame, text="End Time")

        self.label_room.grid(row=0, column=0)
        self.label_facilities.grid(row=1, column=0)
        self.label_StaffID.grid(row=2, column=0)
        self.label_Participants.grid(row=3, column=0)
        self.label_startTime.grid(row=4, column=0)
        self.label_endTime.grid(row=5, column=0)

    def show(self, column):
        self.label_room.grid(row=self.row, column=column)
        self.lb_queue.grid_forget()

    def hide(self):
        self.label_room.grid_forget()
        self.lb_queue.grid_forget()





class LoginWindow():

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.label_welcome = Label(self.frame, text="Welcome")
        self.label_welcome.grid(row=0, column=1)

        self.btn_booking = Button(self.frame, text="Make Booking", command=self.make_booking)
        self.btn_booking.grid(row=1, column=0)
        #self.btn_remove = Button(self.frame, text="Remove Booking", command=self.remove_booking)
        #self.btn_remove.grid(row=1, column=1)

    def show(self):
        self.frame.grid(row=0, column=0)

    def hide(self):
        self.frame.grid_forget()

    def make_booking(self):
        book = Booking(self.master)
        self.hide()
        book.show()



root = Tk()
#main_window =

root.geometry("1000x800")

login = LoginWindow(root)
login.show()
root.mainloop()

#cur.close()
#conn.close()



