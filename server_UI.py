import tkinter as tk

class ServerUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("ClassroomBookingSystemUI")
        # icon = tk.PhotoImage(file='directory') If you want an icon to be added.
        # self.master.iconphoto(False, icon)
        self.master.geometry("500x500") # Arbitrary size for now
        self.master.resizable(True, True)
        self.pack()

        # TODO: Create labels and buttons. Should be gridded.

    # TODO: Database query functions.
    def add_user(self):
        pass
    def remove_user(self):
        pass
    def add_classroom(self):
        pass
    def remove_classroom(self):
        pass
    def add_equipment(self):
        pass
    def remove_equipment(self):
        pass
    def add_time_period(self):
        pass
    def remove_time_period(self):
        pass
    def add_booking(self):
        pass
    def remove_booking(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ServerUI(master=root)
    root.mainloop()