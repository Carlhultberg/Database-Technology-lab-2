class Personal_Details_Remove():

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master, width=55, height=10)

        master.wm_title("")

        self.label_persons = Label(self.frame, text="Select your name.")
        self.label_persons.grid(row=1, column=0)

        self.all_persons = Listbox(self.frame, selectmode=SINGLE)
        self.all_persons.config(exportselection=False)
        self.all_persons.config(width=55, height=10)
        self.all_persons.bind("<<ListBoxSelect>>", self.choose_name)
        self.all_persons.grid(row=10, column=0)

        self.person_times = Listbox(self.frame, selectmode=SINGLE)
        self.person_times.config(exportselection=False)
        self.person_times.config(width=55, height=10)
        self.person_times.bind("<<ListBoxSelect>>", self.choose_time)
        self.person_times.grid(row=25, column=0)

        self.go_back_buttom = Button(self.frame, text="Go back", command=self.go_back)
        self.go_back_buttom.grid(row=0, column=0)
        self.confirm_booking_buttom = Button(self.frame, text="Confirm Name", command=self.choose_name)
        self.confirm_booking_buttom.grid(row=4, column=0)
        self.confirm_time_buttom = Button(self.frame, text="Choose Time", command=self.choose_time)
        self.confirm_time_buttom.grid(row=22, column=0)

        cur.execute("SELECT fname, lname, staff_id FROM person")
        self.person = cur.fetchall()

        column = 0
        for i in self.person:
            self.all_persons.insert(END, i)
            column += 1

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
        person_id = self.all_persons.get(selections[0])
        selections = [int(x) + 1 for x in selections]
        print("person index:", selections, ": '%s'" % person_id[2])
        person_id = person_id[2]
        #cur.execute("SELECT * FROM current_bookings WHERE staff_id = %s", (person_id,)) #, to make iterable
        cur.execute(" SELECT booking_id, booking_timing, booking_date FROM current_bookings WHERE staff_id = %s", (person_id,))

        self.times = cur.fetchall()
        column = 0
        for i in self.times:
            self.person_times.insert(END,i)
            column +=1

    def choose_time(self):
        self.selections = self.person_times.curselection()
        self.start_time = self.person_times.get(self.selections[0])
        self.selections = [int(x) + 1 for x in self.selections]
        print("time index:", self.selections, ": '%s'" % self.start_time[1])
        self.start_time = str(self.start_time[1])

        cur.execute(
            sql.SQL("DELETE FROM current_bookings WHERE booking_timing = (%s)"),
            [self.start_time])
        conn.commit()

        window = DeletionView(self.master)
        self.hide()
        window.show()

<<<<<<< Updated upstream

class DeletionView():
=======
class LoginWindow():

>>>>>>> Stashed changes
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master, width=55, height=10)
        master.wm_title("")
        self.label_available_times = Label(self.frame, text="Your booking has succesfully been deleted!")
        self.label_available_times.grid(row=0, column=0)
        self.label_available_times.pack()
        self.label_available_times.config(width=55, height=10)

<<<<<<< Updated upstream
        self.go_back_buttom = Button(self.frame, text="Go back to Main Menu", command=self.go_back)
        self.go_back_buttom.grid(row=1, column=0)
        self.go_back_buttom.pack()
=======
        self.btn_booking = Button(self.frame, text="Make Booking", command=self.make_booking)
        self.btn_booking.grid(row=1, column=0)
        self.btn_remove = Button(self.frame, text="Remove Booking", command=self.remove_booking)
        self.btn_remove.grid(row=1, column=1)
>>>>>>> Stashed changes

    def show(self):
        self.frame.grid(row=0, column=0)

    def hide(self):
        self.frame.grid_forget()

    def go_back(self):
        window = Welcome_Window(self.master)
        self.hide()
<<<<<<< Updated upstream
        window.show()
        
        
class Welcome_Window():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master, width=55, height=10)
=======
        t.show()
    def remove_booking(self):
        t = RoomView(self.master)
        self.hide()
        t.show()
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
    def remove_room(self):
        window = Personal_Details_Remove(self.master)
        self.hide()
        window.show()

=======
root.mainloop()
>>>>>>> Stashed changes

def main():
    root = Tk()
    root.geometry("500x500")
    welcome = Welcome_Window(root)
    welcome.show()
    root.mainloop()
    cur.close()
    conn.close()


if __name__ == "__main__":
    db = Connect_Database("localhost", "postgres", "Carlhultberg", "")
    main()
