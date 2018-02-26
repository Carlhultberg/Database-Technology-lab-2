from tkinter import *
import pprint
# import pandas as pd
import time
from tkinter import messagebox
import datetime
import re
import os
import psycopg2
from psycopg2 import sql
from datetime import *
import psycopg2.extensions

conn = psycopg2.connect("host=localhost dbname=room_booking")
cur = conn.cursor()


class Connect_Database():
    def __init__(self, host, dbname, user, password):
        conn_string = "host='" + host + "' dbname='" + dbname + "' user='" + user + "' password='" + password + "'"
        self.connection = psycopg2.connect(conn_string)
        self.cursor = self.connection.cursor()

    def select(self, command):
        self.cursor.execute(command)
        return self.cursor.fetchall()


class Booking_Details():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master, width=55, height=10)

        master.wm_title("")

        self.label_available_rooms = Label(self.frame, text="Choose between available rooms and facilities.")
        self.label_available_rooms.grid(row=1, column=0)

        self.available_rooms = Listbox(self.frame, selectmode=SINGLE)
        self.available_rooms.config(exportselection=False)
        self.available_rooms.config(width=55, height=25)
        self.available_rooms.bind("<<ListBoxSelect>>", self.choose_room)
        self.available_rooms.grid(row=10, column=0)

        self.go_back_buttom = Button(self.frame, text="Go back", command=self.go_back)
        self.go_back_buttom.grid(row=0, column=0)
        self.OK_buttom = Button(self.frame, text="OK", command=self.choose_room)
        self.OK_buttom.grid(row=3, column=0)

        self.requested_time = "18:00:00"
        # cur.execute("SELECT name, facilities FROM resources WHERE available = 0")      # psycopg2.extensions.string_types

        cur.execute("SELECT name, facilities FROM resources WHERE time_of_booking != %s;", (self.requested_time,))

        # cur.execute("SELECT * FROM data WHERE time_of_booking != ANY(%s);", (self.requested_time,))
        self.rooms = cur.fetchall()

        column = 0
        for i in self.rooms:
            self.available_rooms.insert(END, i)
            column += 1

    def show(self):
        self.frame.grid(row=0, column=0)

    def hide(self):
        self.frame.grid_forget()

    def go_back(self):
        window = Welcome_Window(self.master)
        self.hide()
        window.show()

    def go_next(self):
        window = Welcome_Window(self.master)
        self.hide()
        window.show()

    def choose_room(self):
        selections = self.available_rooms.curselection()
        value = self.available_rooms.get(selections)
        selections = [int(x) + 1 for x in selections]
        print("selection index:", selections, ": '%s'" % str(value))

        # Go to next window
        window = Personal_Details(self.master)
        self.hide()
        window.show()


class Personal_Details():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master, width=55, height=10)

        master.wm_title("")

        self.label_persons = Label(self.frame, text="Select your name and project team.")
        self.label_persons.grid(row=1, column=0)

        self.all_persons = Listbox(self.frame, selectmode=SINGLE)
        self.all_persons.config(exportselection=False)
        self.all_persons.config(width=55, height=10)
        self.all_persons.bind("<<ListBoxSelect>>", self.choose_name)
        self.all_persons.grid(row=10, column=0)

        self.all_teams = Listbox(self.frame, selectmode=SINGLE)
        self.all_teams.config(exportselection=False)
        self.all_teams.config(width=55, height=10)
        self.all_teams.bind("<<ListBoxSelect>>", self.choose_team)
        self.all_teams.grid(row=21, column=0)

        self.go_back_buttom = Button(self.frame, text="Go back", command=self.go_back)
        self.go_back_buttom.grid(row=0, column=0)
        self.confirm_booking_buttom = Button(self.frame, text="Confirm Name", command=self.choose_name)
        self.confirm_booking_buttom.grid(row=4, column=0)
        self.confirm_booking_buttom = Button(self.frame, text="Confirm Team", command=self.choose_team)
        self.confirm_booking_buttom.grid(row=20, column=0)

        cur.execute("SELECT fname, lname, staff_id FROM person")
        self.person = cur.fetchall()

        column = 0
        for i in self.person:
            self.all_persons.insert(END, i)
            column += 1

        cur.execute("SELECT team_name FROM team")
        self.team = cur.fetchall()

        column1 = 0
        for i in self.team:
            self.all_teams.insert(END, i)
            column1 += 1

    def show(self):
        self.frame.grid(row=0, column=0)

    def hide(self):
        self.frame.grid_forget()

    def go_back(self):
        window = Welcome_Window(self.master)
        self.hide()
        window.show()

    def choose_name(self):
        selections = self.all_persons.curselection()
        person_name = self.all_persons.get(selections[0])
        selections = [int(x) + 1 for x in selections]
        print("person index:", selections, ": '%s'" % person_name[0])

        # cur.execute(sql.SQL("insert into {} values (%s) where booking_id = 1").format(sql.Identifier('current_bookings')),[self.person_name])
        # conn.commit()

    def choose_team(self):
        team_selections = self.all_teams.curselection()
        team_name = self.all_teams.get(team_selections[0])
        team_selections = [int(x) + 1 for x in team_selections]
        print("team index:", team_selections, ": '%s'" % team_name[0])

        # cur.execute(
        # sql.SQL("insert into {} values (%s) where booking_id = 1").format(sql.Identifier('current_bookings')), [self.team_name])
        # conn.commit()

        # Go to next window
        window = Welcome_Window(self.master)
        self.hide()
        window.show()

        # select staff id where person = chosen person
        # add row in table meet_id = ?, staff_id =


class Show_Times():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master, width=55, height=10)
        self.start_time = "00:00:00"
        self.selections = None
        master.wm_title("")

        self.label_available_times = Label(self.frame, text="When do you need a room today? Specify start time for 1h.")
        self.label_available_times.grid(row=1, column=0)

        self.available_times = Listbox(self.frame, selectmode=SINGLE)
        self.available_times.config(exportselection=False)
        self.available_times.config(width=55, height=25)
        self.available_times.bind("<<ListBoxSelect>>", self.choose_time)
        self.available_times.grid(row=10, column=0)

        self.go_back_buttom = Button(self.frame, text="Go back", command=self.go_back)
        self.go_back_buttom.grid(row=0, column=0)

        self.OK_buttom = Button(self.frame, text="OK", command=self.choose_time)
        self.OK_buttom.grid(row=3, column=0)

        cur.execute("SELECT times FROM available_times")
        self.times = cur.fetchall()

        column = 0
        for i in self.times:
            self.available_times.insert(END, i)
            column += 1

    # Todo. If no available rooms add a loop that tells the user that.

    def show(self):
        self.frame.grid(row=0, column=0)

    def hide(self):
        self.frame.grid_forget()

    def go_back(self):
        window = Welcome_Window(self.master)
        self.hide()
        window.show()

    def choose_time(self):
        self.selections = self.available_times.curselection()
        self.start_time = self.available_times.get(self.selections[0])
        self.selections = [int(x) + 1 for x in self.selections]
        print("time index:", self.selections, ": '%s'" % self.start_time[0])
        self.start_time = str(self.start_time[0])

        cur.execute(
            sql.SQL("insert into {} values (%s) where booking_id = 1").format(sql.Identifier('current_bookings')),
            [self.start_time])
        conn.commit()

        window = Booking_Details(self.master)
        self.hide()
        window.show()


class Welcome_Window():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master, width=55, height=10)

        master.wm_title("")
        self.start_label = Label(self.frame, text="Choose your action.")
        self.start_label.grid(row=0, column=1)
        self.start_label.pack()
        self.start_label.config(width=55, height=10)

        self.book_buttom = Button(self.frame, text="Book Room", command=self.book_room)
        self.book_buttom.grid(row=1, column=0)
        self.book_buttom.pack()

        self.remove_buttom = Button(self.frame, text="Remove Room", command=self.remove_room)
        self.remove_buttom.grid(row=1, column=2)
        self.remove_buttom.pack()

    def show(self):
        self.frame.grid(row=0, column=0)

    def hide(self):
        self.frame.grid_forget()

    def book_room(self):
        window = Show_Times(self.master)
        self.hide()
        window.show()

    def remove_room(self):
        window = Booking_Details(self.master)
        self.hide()
        window.show()


def main():
    root = Tk()
    root.geometry("500x500")
    welcome = Welcome_Window(root)
    welcome.show()
    root.mainloop()
    cur.close()
    conn.close()


if __name__ == "__main__":
    db = Connect_Database("localhost", "room_booking", "annahedstrom", "")
    main()



