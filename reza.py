import tkinter as tk
from tkinter import ttk
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='my_contacts'
)
cursor = db.cursor()


class Example:
    def __init__(self):
        window.title('Phika')
        window.geometry('500x400')
        window.wm_minsize(100, 100)

        self.Quitbtn = ttk.Button(window, text='Quit', command=self.close)
        self.Quitbtn.place(x=415, y=365)

        self.save_btn = ttk.Button(window, text='Save', command=self.save)
        self.save_btn.place(x=330, y=365)

        # Labels ------------------------------------------
        self.name_label = ttk.Label(window, text='Name')
        self.name_label.place(x=20, y=50)

        self.family_label = ttk.Label(window, text='Family')
        self.family_label.place(x=20, y=100)

        self.phone_label = ttk.Label(window, text='Phone')
        self.phone_label.place(x=20, y=150)

        # Entry -------------------------------------------
        name = tk.StringVar()
        global name_entry
        name_entry = tk.Entry(window, textvariable=name, width=20)
        name_entry.place(x=100, y=50)

        family = tk.StringVar()
        global family_entry
        family_entry = tk.Entry(window, textvariable=family, width=20)
        family_entry.place(x=100, y=100)

        phone = tk.IntVar()
        global phone_entry
        phone_entry = tk.Entry(window, textvariable=phone, width=20)
        phone_entry.place(x=100, y=150)

    @staticmethod
    def close():
        db.close()
        window.quit()

    @staticmethod
    def save():
        name = name_entry.get()
        family = family_entry.get()
        phone = phone_entry.get()

        cursor.execute("insert into list1 (name, family, phone_number) values ('{}', '{}', '{}')".
                       format(name, family, phone))
        db.commit()

        tk.Label(window, text='Saved Successfully!', fg='green', font=20).place(x=100, y=350)


window = tk.Tk()
obj = Example()  # object instantiated
window.mainloop()
