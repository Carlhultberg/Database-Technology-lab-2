
from tkinter import *
#import pymysql as mdb
#import pandas as pd
import time
from tkinter import messagebox
import datetime
import re
import os
import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres")
cur = conn.cursor()


class RoomView():
    def __init__(self,master):
        self.master = master
        self.frame = Frame(master)

        self.lb_room = Listbox(self.frame, selectmode=SINGLE)
        self.label_Participants = Label(self.frame, text="Participants")
        self.label_Participants.grid(row=1, column=2)
        self.lb_room.config(exportselection=False) #no deselect when clicking outside box
        self.lb_room.config(width=50, height=20)
        self.lb_room.bind('<<ListBoxSelect>>', self.selected_room)
        self.lb_room.grid(row=20, column=2)
        self.btn_booking = Button(self.frame, text="Go back to start", command=self.Back_menu)
        self.btn_booking.grid(row=0, column=2)

        cur.execute("SELECT Resources.Room_ID, Stuff, Cost FROM Resources INNER JOIN Facilities ON Resources.Room_ID = Facilities.Room_ID WHERE IsBooked = 0")
        rooms = cur.fetchall()
        column = 0
        for room in rooms:
            self.lb_room.insert(END, room)
            column += 1

    def show(self):
        self.frame.grid(row=0, column=0)


    def hide(self):
        self.frame.grid_forget()

    def Back_menu(self):
        t = LoginWindow(self.master)
        self.hide()
        t.show()

    def selected_room(self, evt):
        w = evt.widget
        index = int(w.curseselection()[0])
        room = w.get(index)

        self.hide()

class RemoveView():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)

        self.lb_room = Listbox(self.frame, selectmode=SINGLE)
        self.lb_room.config(exportselection=FALSE)
        self.lb_room.bind('<<ListBoxSelect>>', self.select_booked_room)
        self.lb_room.grid(row=0,column=0)
        self.btn_booking = Button(self.frame, text="Go back to start", command=self.Back_menu)
        self.btn_booking.grid(row=1, column=6)

        cur.execute("SELECT * FROM room")
        rooms = cur.fetchall()
        for room in rooms:
            self.lb_room.insert(END, room)


    def show(self):
        self.frame.grid(row=0, column=0)

    def hide(self):
        self.frame.grid_forget()

    def Back_menu(self):
        t = LoginWindow(self.master)
        self.hide()
        t.show()

    def select_booked_room(self, evt):
        w = evt.widget
        index = int(w.curseselection()[0])
        room = w.get(index)

        self.hide()


class LoginWindow():

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.label_welcome = Label(self.frame, text="Welcome")
        self.label_welcome.grid(row=0, column=1)

        self.btn_booking = Button(self.frame, text="Make Booking", command=self.make_booking)
        self.btn_booking.grid(row=2, column=0)
        self.btn_remove = Button(self.frame, text="Remove Booking", command=self.remove_booking)
        self.btn_remove.grid(row=2, column=1)

    def show(self):
        self.frame.grid(row=0, column=0)

    def hide(self):
        self.frame.grid_forget()

    def make_booking(self):
        t = RoomView(self.master)
        self.hide()
        t.show()

    def remove_booking(self):
        t = RemoveView(self.master)
        self.hide()
        t.show()


root = Tk()

#main_window =

root.geometry("1000x800")

login = LoginWindow(root)
login.show()



root.mainloop()


cur.close()
conn.close()

