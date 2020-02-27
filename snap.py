import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
from dbase import Database
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
# from cryptography.fernet import Fernet
import decimal
import sys
import os
import random
import base64
import time
import sqlite3
import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

# from cryptography.fernet import Fernet
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

db = Database('saved.db')


######### Potentially use selenium to upload a csv from a button click. clears everything as well then auto uploads to the cloud for me.


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, *sys.argv)


# key1 = Fernet.generate_key()
# cs = Fernet(key1)
#
# key = Fernet.generate_key()
# cipher_suite = Fernet(key)
#
# def my_encrypt(key, data):
#     f = Fernet(key)
#     return f.encrypt(data.encode('utf-8'))


# def my_decrypt(key, data):
#     f = Fernet(key)
#     return f.decrypt(data) 
# def encryuser(data):
#     key = Fernet.generate_key()
#     f = Fernet(key)
#     what = data
#     what_b = str.encode(what)
#     token = f.encrypt(what_b)
#     file1 = '/Users/Snapshot/Downloads/Expense-App-master/junk/stringu'
#     file2 = '/Users/Snapshot/Downloads/Expense-App-master/junk/keyu'
#     with open(file1, "wb") as f1, open(file2, "wb") as f2:
#         f1.write(token)
#         f2.write(key)
#
# def encrypass(data):
#     key = Fernet.generate_key()
#     f = Fernet(key)
#     what = data
#     what_b = str.encode(what)
#     token = f.encrypt(what_b)
#     file1 = '/Users/Snapshot/Downloads/Expense-App-master/junk/stringp'
#     file2 = '/Users/Snapshot/Downloads/Expense-App-master/junk/keyp'
#     with open(file1, "wb") as f1, open(file2, "wb") as f2:
#         f1.write(token)
#         f2.write(key)
#
#
# def decryuser():
#     file1 = '/Users/Snapshot/Downloads/Expense-App-master/junk/stringu'
#     file2 = '/Users/Snapshot/Downloads/Expense-App-master/junk/keyu'
#
#     with open(file1, "rb") as f1, open(file2, "rb") as f2:
#         token = f1.read()
#         key = f2.read()
#
#     f = Fernet(key)
#     what_d = str(f.decrypt(token),'utf-8')
#     return what_d
#
# def decrypass():
#     file1 = '/Users/Snapshot/Downloads/Expense-App-master/junk/stringp'
#     file2 = '/Users/Snapshot/Downloads/Expense-App-master/junk/keyp'
#
#     with open(file1, "rb") as f1, open(file2, "rb") as f2:
#         token = f1.read()
#         key = f2.read()
#
#     f = Fernet(key)
#     what_d = str(f.decrypt(token),'utf-8')
#     return what_d

class Master(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.style = ThemedStyle(self)
        self.style.set_theme('scidblue')

        # for F in (Login, HomePage, Sales, Owing, Summary, Expense, Pricing):
        for F in (HomePage, Sales, Owing, Summary, Expense, Pricing):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # self.show_frame(Login)
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# class Login(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self,parent)
#         self.style = ThemedStyle(self)
#         self.style.set_theme('scidblue')
#         self.controller = controller
#         self.login_widgets()
#
#     def login_widgets(self):
#         self.document = ImageTk.PhotoImage(Image.open(resource_path('images/document.png')))
#
#         label = tk.Label(self, text="Login", font=('Arial 30 bold'))
#         label.configure(foreground='green')
#         label.grid(row=0, column=1, pady=25, padx=500)
#
#         self.personsLabel = tk.Label(self, text='Username', font=('Arial 10 bold'))
#         self.personsLabel.grid(row=1, column=1, padx=25)
#
#         self.username_entry = tk.StringVar()
#         self.username = ttk.Entry(self, width=13, textvariable=self.username_entry)
#         self.username.grid(row=2, column=1, pady=10)
#
#         self.passwordLabel = tk.Label(self, text='Password', font=('Arial 10 bold'))
#         self.passwordLabel.grid(row=3, column=1, padx=25)
#
#         self.password_entry = tk.StringVar()
#         self.password = ttk.Entry(self, width=13, textvariable=self.password_entry, show="*")
#         self.password.grid(row=4, column=1, pady=10)
#
#         self.buttonlogin = ttk.Button(self, text="  Login", width=10, image=self.document, compound=LEFT, command=self.verify)
#         self.buttonlogin.grid(row=5, column=1, padx=25, pady=25, ipady=5)
#
#         self.button = ttk.Button(self, text="  First Login", width=10, image=self.document, compound=LEFT,
#                                  command=self.first_user)
#         self.button.grid(row=7, column=1, padx=25, pady=25, ipady=5)
#
#         # self.button = ttk.Button(self, text="  Login", width=10, image=self.document, compound=LEFT,
#         #                          command=self.login)
#         # self.button.grid(row=6, column=1, padx=25, pady=25, ipady=5)
#
#         # self.button = ttk.Button(self, text="  First Login", width=10, image=self.document, compound=LEFT, command=self.first_password)
#         # self.button.grid(row=6, column=1, padx=25, pady=25, ipady=5)
#         file1 = '/Users/Snapshot/Downloads/Expense-App-master/junk/stringp'
#         with open(file1) as f:
#             for x in f.readlines():
#                 if len(x) < 1:
#                     self.button
#                     self.button
#                 else:
#                     self.button.destroy()
#
#
#
#     def verify(self):
#         username = self.username_entry.get()
#         user = decryuser()
#         passw = decrypass()
#         password = self.password_entry.get()
#         if username == user and password == passw:
#             # lambda: self.controller.show_frame(HomePage)
#             self.controller.show_frame(HomePage)
#         else:
#             messagebox.showinfo('Error', "Cunt")
#
#     def first_user(self):
#         encryuser(self.username_entry.get())
#         encrypass(self.password_entry.get())
#         time.sleep(1)
#         restart_program()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.style = ThemedStyle(self)
        self.style.set_theme('scidblue')
        self.controller = controller
        self.create_widgets()
        self.populate_list()
        self.button1 = ttk.Button(self, text="< Back", command=lambda: controller.show_frame(Login))
        self.button1.place(x=15, y=15)

        self.document = ImageTk.PhotoImage(Image.open(resource_path('images/document.png')))
        self.bookmark = ImageTk.PhotoImage(Image.open(resource_path('images/bookmark.png')))
        self.briefcase = ImageTk.PhotoImage(Image.open(resource_path('images/briefcase.png')))
        self.expense = ImageTk.PhotoImage(Image.open(resource_path('images/expense.png')))
        self.info = ImageTk.PhotoImage(Image.open(resource_path('images/info.png')))
        self.restart = ImageTk.PhotoImage(Image.open(resource_path('images/restart.png')))
        self.settings = ImageTk.PhotoImage(Image.open(resource_path('images/settings.png')))

        self.persons1Label = tk.Label(self, text='1', font='Arial 2 bold')
        self.persons1Label.grid(row=1, column=0, padx=125, rowspan=5)

        label = tk.Label(self, text="Expense App", font='Arial 30 bold')
        label.configure(foreground='green')
        label.grid(row=0, column=1, columnspan=10, pady=10, padx=50)

        button = ttk.Button(self, text="  Sales", width=10, image=self.document, compound=LEFT,
                            command=lambda: controller.show_frame(Sales))
        button.grid(row=1, column=1, padx=25, pady=25, ipady=5)

        button2 = ttk.Button(self, text="  Owing", width=10, image=self.bookmark, compound=LEFT,
                             command=lambda: controller.show_frame(Owing))
        button2.grid(row=1, column=2, padx=25, pady=25, ipady=5)

        button3 = ttk.Button(self, text="  Summary", width=10, image=self.info, compound=LEFT,
                             command=lambda: controller.show_frame(Summary))
        button3.grid(row=1, column=3, padx=25, pady=25, ipady=5)

        button4 = ttk.Button(self, text="  Expense", width=10, image=self.expense, compound=LEFT,
                             command=lambda: controller.show_frame(Expense))
        button4.grid(row=2, column=1, padx=25, pady=25, ipady=5)

        button4 = ttk.Button(self, text="  Pricing", width=10, image=self.settings, compound=LEFT,
                             command=lambda: controller.show_frame(Pricing))
        button4.grid(row=2, column=2, padx=25, pady=25, ipady=5)
        restartButton = ttk.Button(self, width=10, text="  Restart", image=self.restart, compound=LEFT,
                                   command=restart_program)
        restartButton.grid(row=2, column=3, ipady=5)

    def create_widgets(self):
        # Tree View
        self.balanceTree = ttk.Treeview(self, height=10, columns='id')
        self.balanceTree.heading('#0', text='Account', anchor=tk.CENTER)
        self.balanceTree.heading('#1', text='Current', anchor=tk.CENTER)
        self.balanceTree.column('#0', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.balanceTree.column('#1', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.balanceTree.grid(row=3, column=1, columnspan=5, pady=15)

    def populate_list(self):
        for main in db.transactionFetch():
            self.balanceTree.insert('', 0, text=main[0], values=main[1])


class Sales(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.style = ThemedStyle(self)
        self.style.set_theme('scidblue')
        self.controller = controller
        self.create_widgets()
        self.refresh()
        self.populateReportList()

        self.listed = []

        self.button1 = ttk.Button(self, text="< Back", command=lambda: controller.show_frame(HomePage))
        self.button1.place(x=15, y=15)

    def create_widgets(self):
        self.value, self.coin = [], []
        for x in db.mainfetch():
            self.value.append(x[0])
            self.coin.append(x[1])

        self.trash = ImageTk.PhotoImage(Image.open(resource_path('images/trash.png')))
        self.check = ImageTk.PhotoImage(Image.open(resource_path('images/check.png')))
        self.restart = ImageTk.PhotoImage(Image.open(resource_path('images/restart.png')))

        self.category_values = ['Business', 'Personal Profits', 'Round Up', 'Oranges', 'Bonus', 'Others']
        self.titleLabel = tk.Label(self, text='Sales', font='Arial 30 bold')
        self.titleLabel.grid(row=0, column=1, pady=10, columnspan=7)
        self.titleLabel.configure(foreground='green')

        # Person Label/Title
        self.personsLabel = tk.Label(self, text='Payee', font='Arial 10 bold')
        self.personsLabel.grid(row=1, column=0, padx=25)

        # Persons Input Box, Could put a auto complete box after we get a list.
        self.persons_entry = tk.StringVar()
        self.personEntry = ttk.Entry(self, width=15, textvariable='persons_entry')
        self.personEntry.grid(row=2, column=0, pady=10, padx=25)

        # from Label/Title
        self.from_label = tk.Label(self, text='From', font='Arial 10 bold')
        self.from_label.grid(row=1, column=1)
        # from dropdown box and selection
        self.from_combo = tk.StringVar()
        self.fromCombo = ttk.Combobox(self, width=10, values=self.value, textvariable=self.from_combo)
        # self.fromCombo.bind('<<ComboboxSelected>>', self.currentBalanceLabels)
        self.fromCombo.grid(row=2, column=1, pady=10, padx=25)

        # To Label/Title
        self.to_label = tk.Label(self, text='To', font='Arial 10 bold')
        self.to_label.grid(row=1, column=2)
        # To dropdown box and selection
        self.to_combo = tk.StringVar()
        self.toCombo = ttk.Combobox(self, width=10, values=self.value, textvariable=self.to_combo)
        self.toCombo.grid(row=2, column=2, pady=10, padx=25)

        # Amount Label/Title
        self.amount_label = tk.Label(self, text='Amount', font='Arial 10 bold')
        self.amount_label.grid(row=1, column=3)
        # To dropdown box and selection
        self.amount_entry = tk.IntVar()
        # self.amount_entry = tk.StringVar()
        self.amount_entry.trace('w', self.mitsi_tracer)
        self.amount_entry.trace('w', self.oranges_tracer)
        self.amount_entry.trace('w', self.mazda_tracer)
        self.amount_entry.trace('w', self.citeron_tracer)

        self.amountEntry = ttk.Entry(self, width=10, textvariable=self.amount_entry)
        self.amountEntry.grid(row=2, column=3, pady=10, padx=25)

        # To Label/Title
        self.profit_label = tk.Label(self, text='Profit', font='Arial 10 bold')
        self.profit_label.grid(row=1, column=4)
        # To dropdown box and selection
        self.profit_entry = tk.StringVar()
        self.t_var = tk.IntVar()
        self.profitEntry = tk.Label(self, textvariable=self.t_var)
        # self.toCombo.bind('<<ComboboxSelected>>', self.afterBalanceLabels)
        self.profitEntry.grid(row=2, column=4, pady=10, padx=25)

        # To Label/Title
        self.category_label = tk.Label(self, text='Category', font='Arial 10 bold')
        self.category_label.grid(row=1, column=5)
        # To dropdown box and selection
        self.category_combo = tk.StringVar()
        self.categoryCombo = ttk.Combobox(self, width=10, values=self.category_values, textvariable=self.category_combo)
        self.categoryCombo.grid(row=2, column=5, pady=10, padx=25)

        # Enter Button
        self.enterButton = ttk.Button(self, width=10, image=self.check, compound=LEFT, text='  Enter',
                                      command=self.insert)
        self.enterButton.grid(row=4, column=0, ipady=5)

        # Refresh Button
        self.refreshButton = ttk.Button(self, width=10, image=self.restart, compound=LEFT, text='  Clear',
                                        command=self.clear)
        self.refreshButton.grid(row=6, column=0, ipady=5)

        # Remove Button
        self.removeButton = ttk.Button(self, width=10, image=self.trash, compound=LEFT, text='  Remove',
                                       command=self.remove)
        self.removeButton.grid(row=5, column=0, ipady=5)

        # Mitsi Entry
        self.mitsi_entry = tk.DoubleVar()
        self.mitsi_entry.trace('w', self.mitsi_tracer)
        self.mitsi_entry.trace('w', self.oranges_tracer)
        self.mitsi_entry.trace('w', self.mazda_tracer)
        self.mitsi_entry.trace('w', self.citeron_tracer)
        self.mitsiEntry = ttk.Entry(self, width=10, textvariable=self.mitsi_entry)
        self.mitsiEntry.grid(row=3, column=1)

        # Tree View
        self.tree = ttk.Treeview(self, height=20, columns=('id', 'items', 'total', 'quantity', 'category'))
        self.tree.heading('#0', text='Payee', anchor=tk.CENTER)
        self.tree.heading('#1', text='From', anchor=tk.CENTER)
        self.tree.heading('#2', text='To', anchor=tk.CENTER)
        self.tree.heading('#3', text='Amount', anchor=tk.CENTER)
        self.tree.heading('#4', text='Profit', anchor=tk.CENTER)
        self.tree.heading('#5', text='Category', anchor=tk.CENTER)
        self.tree.column('#0', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.tree.column('#1', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.tree.column('#2', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.tree.column('#3', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.tree.column('#4', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.tree.column('#5', stretch=tk.YES, minwidth=50, width=150, anchor='center')
        self.tree.grid(row=4, column=1, columnspan=10, padx=20, pady=20, rowspan=5)
        self.tree.bind('<ButtonRelease-1>', self.select_item)

    def select_all(self):
        self.curItems = self.tree.selection()
        lst = []
        for i in self.curItems:
            items = self.tree.item(i)['values']
            # print(items)
            lst.append(items)
        print(lst)
        print(lst[0])

    def populateReportList(self):
        for self.row in db.reportfetch():
            self.tree.insert('', 0, text=self.row[0], values=(
            self.row[1], self.row[2], self.row[3], self.row[4], self.row[5], self.row[6], self.row[0]))
            # Payeee                #from       #to             #amount     #profit       #category     #id

    def mitsi_tracer(self, a, b, c):
        # print a, b, c
        value, price = [], []
        for x in db.pricingfetch():
            value.append(x[1])
            price.append(x[2])
        mitsi, oranges, citeron, mazda = price[0], price[2], price[1], price[3]
        amt_int = int(self.amount_entry.get())
        amount = amt_int
        mitsi1 = self.mitsi_entry.get()
        yeet = mitsi1 * mitsi
        derp = amount - yeet
        new_text = derp
        self.t_var.set(new_text)

    # TODO: Must fix all the tracers but mitsubishi. pulling incorrect numbers
    def oranges_tracer(self, a, b, c):
        # print a, b, c
        value, price = [], []
        for x in db.pricingfetch():
            value.append(x[1])
            price.append(x[2])
        mitsi, oranges, citeron, mazda = price[0], price[2], price[1], price[3]
        amt_int = int(self.amount_entry.get())
        amount = amt_int
        mitsi1 = self.mitsi_entry.get()
        yeet = mitsi1 * oranges
        derp = amount - yeet
        new_text = derp
        self.t_var.set(new_text)

    # TODO: Must fix all the tracers but mitsubishi. pulling incorrect numbers
    def citeron_tracer(self, a, b, c):
        # print a, b, c
        value, price = [], []
        for x in db.pricingfetch():
            value.append(x[1])
            price.append(x[2])
        mitsi, oranges, citeron, mazda = price[0], price[2], price[1], price[3]
        amt_int = int(self.amount_entry.get())
        amount = amt_int
        mitsi1 = self.mitsi_entry.get()
        yeet = mitsi1 * citeron
        derp = amount - yeet
        new_text = derp
        self.t_var.set(new_text)

    # TODO: Must fix all the tracers but mitsubishi. pulling incorrect numbers
    def mazda_tracer(self, a, b, c):
        # print a, b, c
        value, price = [], []
        for x in db.pricingfetch():
            value.append(x[1])
            price.append(x[2])
        mitsi, oranges, citeron, mazda = price[0], price[2], price[1], price[3]
        amt_int = int(self.amount_entry.get())
        amount = amt_int
        mitsi1 = self.mitsi_entry.get()
        yeet = mitsi1 * mazda
        derp = amount - yeet
        new_text = derp
        self.t_var.set(new_text)

    def deleteallItem(self):
        confirmed = tk.messagebox.askyesno('Please Confirm', 'Do you want to delete all?')
        if confirmed == True:
            self.remove()
        elif confirmed == False:
            print('Ok')

    # TODO: Upgrade this function to then remove multi selected items please use selectall as a reference. as to how to achieve this
    def remove(self):
        confirmed = tk.messagebox.askyesno('Please Confirm', 'Do you want to delete this item?')
        if confirmed == True:
            self.conn = sqlite3.connect('saved.db')
            self.s_item = self.tree.focus()
            self.delete_list = []
            tree = self.tree.item(self.s_item)
            for k, v in tree.items():
                self.delete_list.append(v)
            deleted = self.delete_list
            print(f"Successfully removed from the Database: Name: {deleted[0]} {deleted[2]} {deleted[1]}")
            db.remove_profit(self.row[4], self.row[5], self.row[3])
            db.remove_amount_fromto(self.row[3], self.derp)
            self.cur = self.conn.cursor()
            for self.selected_item in self.tree.selection():
                # items = self.tree.item(i)['values']
                self.cur.execute("DELETE FROM report WHERE id=?", (self.derp,))
                self.conn.commit()
            self.conn.close()
            for i in self.tree.get_children():
                self.tree.delete(i)
            self.populateReportList()
        elif confirmed == False:
            print('Ok')

    def refresh(self):
        if self.from_combo.get() == "Mitsubishi":
            self.mitsi_tracer()
        elif self.from_combo.get() == "Oranges":
            self.oranges_tracer()
        elif self.from_combo.get() == "Mazdas":
            self.mazda_tracer()
        elif self.from_combo.get() == "Citeron":
            self.citeron_tracer()

    def clear(self):
        self.mitsiEntry.delete(0, 'end')
        tex = 0
        self.t_var.set(tex)
        self.personEntry.delete(0, 'end')

    def refresh_list(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.populateReportList()

    def insert_into_table(self):
        payee = self.personEntry.get()
        fromm = self.from_combo.get()
        to = self.to_combo.get()
        amount = self.amount_entry.get()
        profit = int(self.t_var.get())
        category = self.category_combo.get()
        db.transaction(amount, fromm, to)
        db.positive(category, profit)
        db.insert(payee, fromm, to, amount, profit, category, random.randint(1, 10000))
        db.re_insert(profit, fromm)
        print(f"Successfully transfered from accounts {fromm} to {to} ")
        print(f"Successfully added {profit} to the account {to}")

    def insert(self):
        payee = self.personEntry.get()
        fromm = self.from_combo.get()
        too = self.to_combo.get()
        amount = self.amount_entry.get()
        profit = self.t_var.get()
        category = self.category_combo.get()
        if too == 'Toyota':
            self.insert_into_table()
            db.outstanding_insert(payee, amount)
            print(f"Successfully added to {payee}'s outstanding balance. ")
            self.refresh_list()
        else:
            try:
                self.insert_into_table()
            except sqlite3.IntegrityError:
                print(f"Please restart the programme, you tried to transfer an amount more than what is in there")
            self.refresh_list()

    def select_item(self, event):
        self.selectItem = self.tree.focus()
        self.my_list = []
        tree = self.tree.item(self.selectItem)
        for k, v in tree.items():
            self.my_list.append(v)
        self.derp = self.my_list[2][5]
        # yeet = derp[0]
        cars = self.my_list[0]
        print(self.derp)
        # # print(yeet)
        # print(cars)


class Owing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.style = ThemedStyle(self)
        self.style.set_theme('scidblue')
        self.controller = controller
        self.owing_widgets()
        self.populate_owing()

        self.button1 = ttk.Button(self, text="< Back", command=lambda: controller.show_frame(HomePage))
        self.button1.place(x=25, y=25)

    def owing_widgets(self):
        # Owing Label
        self.ticklistLabel = tk.Label(self, text='')
        self.ticklistLabel.grid(row=0, column=0, pady=10, padx=125)

        self.ticklistLabel = tk.Label(self, text='Outstanding', font='Arial 30 bold')
        self.ticklistLabel.grid(row=1, column=1, pady=10, columnspan=10)
        self.ticklistLabel.configure(foreground='green')

        # Owing labels
        self.payeeLabel = tk.Label(self, text='Payee', font='Arial 10 bold')
        self.payeeLabel.grid(row=3, column=1)
        self.outstandingLabel = tk.Label(self, text='Outstanding', font='Arial 10 bold')
        self.outstandingLabel.grid(row=3, column=2)
        self.payingLabel = tk.Label(self, text='Paying', font='Arial 10 bold')
        self.payingLabel.grid(row=3, column=3)

        # Paid button
        self.paidButton = ttk.Button(self, width=10, text='Paid', command=self.payee_paid)
        self.paidButton.grid(row=4, column=5, pady=25)

        # Owing Enteries
        self.payee_entry = tk.StringVar()
        self.payeeEntry = ttk.Entry(self, width=10, textvariable=self.payee_entry)
        self.payeeEntry.grid(row=4, column=1, pady=25, padx=25)
        self.outstanding_entry = tk.StringVar()
        self.outstandingEntry = ttk.Entry(self, width=10, textvariable=self.outstanding_entry)
        self.outstandingEntry.grid(row=4, column=2, pady=25)
        self.paying_entry = tk.IntVar()
        self.payingEntry = ttk.Entry(self, width=10, textvariable=self.paying_entry)
        self.payingEntry.grid(row=4, column=3, pady=25, padx=25)
        acc_values = ['Coin', 'Bills']
        self.account_combo = tk.StringVar()
        self.accountCombo = ttk.Combobox(self, width=10, values=acc_values, textvariable=self.account_combo)
        self.accountCombo.grid(row=4, column=4)

        # Tree View
        self.owingTree = ttk.Treeview(self, height=10, columns='outstanding')
        self.owingTree.heading('#0', text='Payee', anchor=tk.CENTER)
        self.owingTree.heading('#1', text='Balance', anchor=tk.CENTER)
        self.owingTree.column('#0', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.owingTree.column('#1', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.owingTree.grid(row=2, column=1, columnspan=5, pady=15)
        self.owingTree.bind('<ButtonRelease-1>', self.select_item)

    def populate_owing(self):
        for self.row in db.outstanding_fetch():
            self.owingTree.insert('', 0, text=self.row[0], values=self.row[1])

    def payee_paid(self):
        payee = self.payee_entry.get()
        paying = self.paying_entry.get()
        outstanding = self.outstanding_entry.get()
        account = self.account_combo.get()
        if account == "Coin":
            db.outstanding_transaction(account, paying)
            db.outstanding_paid(payee, paying)
        elif account == "Bills":
            db.outstanding_transaction(account, paying)
            db.outstanding_paid(payee, paying)
        self.refresh_list()
        self.payingEntry.delete(0, END)
        self.payingEntry.insert(END, 0)

    def refresh_list(self):
        for i in self.owingTree.get_children():
            self.owingTree.delete(i)
        self.populate_owing()

    def select_item(self, event):
        self.selectItem = self.owingTree.focus()
        self.my_list = []
        tree = self.owingTree.item(self.selectItem)
        for k, v in tree.items():
            self.my_list.append(v)
        derp = self.my_list[2]
        yeet = derp[0]
        cars = self.my_list[0]
        self.payeeEntry.delete(0, END)
        self.payeeEntry.insert(END, cars)
        self.outstandingEntry.delete(0, END)
        self.outstandingEntry.insert(END, yeet)

    # TODO: Add a remove button for when someone hits 0 in their outstanding


class Summary(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.style = ThemedStyle(self)
        self.style.set_theme('scidblue')
        self.controller = controller
        self.summary_widgets()

        self.button1 = ttk.Button(self, text="< Back", command=lambda: controller.show_frame(HomePage))
        self.button1.place(x=25, y=25)

    def summary_widgets(self):
        # Summary Label
        self.ticklistLabel = tk.Label(self, text='Summary', font='Arial 30 bold')
        self.ticklistLabel.grid(row=0, column=1, pady=15, columnspan=10)
        self.ticklistLabel.configure(foreground='green')

        self.expense = tk.Label(self, text='Expense', font='Arial 15 underline')
        self.expense.grid(row=1, column=0, pady=10)
        self.expenseTotal = tk.Label(self, text='Amount', font='Arial 15 underline')
        self.expenseTotal.grid(row=1, column=1, pady=10)

        self.profit = tk.Label(self, text='Profit', font='Arial 15 underline')
        self.profit.grid(row=1, column=3, pady=10)
        self.profitTotal = tk.Label(self, text='Amount', font='Arial 15 underline')
        self.profitTotal.grid(row=1, column=4, pady=10)

        self.labels = tk.Label(self, text='Stats', font='Arial 15 underline')
        self.labels.grid(row=9, column=3, pady=10)
        self.totals = tk.Label(self, text='Totals', font='Arial 15 underline')
        self.totals.grid(row=9, column=4, pady=10)

        self.balances = tk.Label(self, text='Balances', font='Arial 15 underline')
        self.balances.grid(row=1, column=8, pady=10, padx=15)
        self.accounts = tk.Label(self, text='Accounts', font='Arial 15 underline')
        self.accounts.grid(row=1, column=7, pady=10, padx=15)

        expenseLabel = tk.Label(self, text='Expenses')
        expenseLabel.grid(row=11, column=3)
        positiveLabel = tk.Label(self, text='Incomes')
        positiveLabel.grid(row=10, column=3)
        positivityLabel = tk.Label(self, text='Overall', font='Arial 17')
        positivityLabel.grid(row=13, column=3)
        accountLabel = tk.Label(self, text='Overall', font='Arial 17')
        accountLabel.grid(row=10, column=7)

        sep = tk.ttk.Separator(self, orient=VERTICAL).grid(column=2, row=2, padx=5, rowspan=26, sticky='ns')
        # sep = tk.ttk.Separator(self, orient=VERTICAL).grid(column=5, row=2,padx=5, rowspan=26, sticky='ns')
        sep = tk.ttk.Separator(self, orient=VERTICAL).grid(column=6, row=1, padx=100, rowspan=28, sticky='ns')
        sep1 = tk.ttk.Separator(self, orient=HORIZONTAL).grid(column=3, row=8, columnspan=3, sticky='ew', padx=50)
        sep2 = tk.ttk.Separator(self, orient=HORIZONTAL).grid(column=3, row=12, columnspan=3, sticky='ew', padx=50)
        sep3 = tk.ttk.Separator(self, orient=HORIZONTAL).grid(column=7, row=9, columnspan=2, sticky='ew')

        self.expense_sum = db.expense_total()
        sum = int(self.expense_sum[0][0])
        str_sum = f"{sum:,d}"
        sumLabel = tk.Label(self, text=str_sum)
        sumLabel.grid(row=11, column=4)

        self.positive_sum = db.positive_total()
        sum1 = int(self.positive_sum[0][0])
        str_sum1 = f"{sum1:,d}"
        sumLabel1 = tk.Label(self, text=str_sum1)
        sumLabel1.grid(row=10, column=4)

        self.account_sum = db.account_total()
        self.loan_sum = db.loanfetch()
        self.shitlist = db.shit_list()
        shit = int(self.shitlist[0][0])
        loan_sum = int(self.loan_sum[0][0])
        sum2 = int(self.account_sum[0][0])
        final_amount = sum2 - loan_sum
        rip = final_amount + shit
        str_sum2 = f"{final_amount:,d}"
        str_sum3 = f"{sum2:,d}"
        str_sum4 = f"{rip:,d}"
        sumLabel3 = tk.Label(self, text=str_sum3, font='Arial 17')
        sumLabel3.grid(row=10, column=8)
        sumLabel2 = tk.Label(self, text=str_sum2, font='Arial 17')
        sumLabel2.grid(row=11, column=8)
        sumLabel5 = tk.Label(self, text=str_sum4, font='Arial 12')
        sumLabel5.grid(row=12, column=8)

        final_income = sum1 + sum
        income = f"{final_income:,d}"
        incomeLabel = tk.Label(self, text=income, font='Arial 17')
        incomeLabel.grid(row=13, column=4)

        self.expense_labels = []
        self.expense_totals = []
        for k, v in db.expense_fetch():
            self.expense_labels.append(k)
            v = f"{v:,d}"
            self.expense_totals.append(v)
        for row, list1 in enumerate(self.expense_labels, start=2):
            label = tk.Label(self, text=list1)
            label.grid(row=row, column=0, padx=15)
        for row1, list2 in enumerate(self.expense_totals, start=2):
            label = tk.Label(self, text=list2)
            label.grid(row=row1, column=1, padx=15)

        self.profit_labels = []
        self.profit_totals = []
        for k, v in db.positive_fetch():
            self.profit_labels.append(k)
            v = f"{v:,d}"
            self.profit_totals.append(v)
        for row, list1 in enumerate(self.profit_labels, start=2):
            label = tk.Label(self, text=list1)
            label.grid(row=row, column=3, padx=15)
        for row1, list2 in enumerate(self.profit_totals, start=2):
            label = tk.Label(self, text=list2)
            label.grid(row=row1, column=4, padx=15)

        self.account_labels = []
        self.account_totals = []
        for k, v in db.mainfetch():
            self.account_labels.append(k)
            v = f"{v:,d}"
            self.account_totals.append(v)
        for row, list1 in enumerate(self.account_labels, start=2):
            label = tk.Label(self, text=list1)
            label.grid(row=row, column=7, padx=15)
        for row1, list2 in enumerate(self.account_totals, start=2):
            label = tk.Label(self, text=list2)
            label.grid(row=row1, column=8, padx=15)


class Expense(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.style = ThemedStyle(self)
        self.style.set_theme('scidblue')
        self.controller = controller
        self.expense_widgets()
        self.populateExpenseList()

        self.button1 = ttk.Button(self, text="< Back", command=lambda: controller.show_frame(HomePage))
        self.button1.place(x=25, y=25)

    def expense_widgets(self):
        self.amount_entry = tk.IntVar()
        self.expense_entry = tk.StringVar()
        self.category_combo = tk.StringVar()
        self.account_combo = tk.StringVar()

        self.expense_category = []
        for k, v in db.expense_fetch():
            self.expense_category.append(k)

        # Expense Title label
        self.expenseTitleLabel = tk.Label(self, text='Expenses', font='Arial 30 bold')
        self.expenseTitleLabel.grid(row=0, column=0, pady=10, columnspan=10)
        self.expenseTitleLabel.configure(foreground='green')

        # Labels
        self.expenseLabel = tk.Label(self, text='Expense', font='Arial 10 bold')
        self.expenseLabel.grid(row=1, column=1)
        self.amountLabel = tk.Label(self, text='Amount', font='Arial 10 bold')
        self.amountLabel.grid(row=1, column=2)
        self.categoryLabel = tk.Label(self, text='Category', font='Arial 10 bold')
        self.categoryLabel.grid(row=1, column=4)
        self.accountLabel = tk.Label(self, text='Account', font='Arial 10 bold')
        self.accountLabel.grid(row=1, column=3)

        # Entry Boxes
        self.expenseEntry = ttk.Entry(self, width=15, textvariable=self.expense_entry)
        self.expenseEntry.grid(row=2, column=1, pady=25)
        self.amountEntry = ttk.Entry(self, width=10, textvariable=self.amount_entry)
        self.amountEntry.grid(row=2, column=2, pady=25)

        # Combo box
        acc_values = ['Coin', 'Bills', "Mitsubishi"]
        self.categoryCombo = ttk.Combobox(self, width=15, values=self.expense_category,
                                          textvariable=self.category_combo)
        self.categoryCombo.grid(row=2, column=4)
        self.accountCombo = ttk.Combobox(self, width=10, values=acc_values, textvariable=self.account_combo)
        self.accountCombo.grid(row=2, column=3)

        # Buttons
        self.enterButton = ttk.Button(self, width=10, text='Enter', command=self.enter)
        self.enterButton.grid(row=3, column=1, columnspan=2, pady=10)

        self.removeButton = ttk.Button(self, width=10, text='Remove', command='')
        self.removeButton.grid(row=3, column=3, columnspan=2, pady=10)

        # Tree View
        self.expenseTree = ttk.Treeview(self, height=10,
                                        columns=('expense', 'amount', 'account', 'category', 'balances'))
        self.expenseTree.heading('#0', text='Expense', anchor=tk.CENTER)
        self.expenseTree.heading('#1', text='Amount', anchor=tk.CENTER)
        self.expenseTree.heading('#2', text='Account', anchor=tk.CENTER)
        self.expenseTree.heading('#3', text='Category', anchor=tk.CENTER)
        self.expenseTree.heading('#4', text='Before Balance', anchor=tk.CENTER)
        self.expenseTree.heading('#5', text='After Balance', anchor=tk.CENTER)
        self.expenseTree.column('#0', stretch=tk.YES, minwidth=50, width=150, anchor='center')
        self.expenseTree.column('#1', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.expenseTree.column('#2', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.expenseTree.column('#3', stretch=tk.YES, minwidth=50, width=150, anchor='center')
        self.expenseTree.column('#4', stretch=tk.YES, minwidth=50, width=150, anchor='center')
        self.expenseTree.column('#5', stretch=tk.YES, minwidth=50, width=150, anchor='center')
        self.expenseTree.grid(row=4, column=0, columnspan=6, padx=150, pady=15)
        self.expenseTree.bind('<ButtonRelease-1>', self.select_item)

    def populateExpenseList(self):
        for self.row in db.expensereport_fetch():
            self.expenseTree.insert('', 0, text=self.row[0],
                                    values=(self.row[1], self.row[2], self.row[3], self.row[4], self.row[5]))
            # expense                 #amount       #account    #category     #bfore       #after

    def enter(self):
        self.amount = self.amount_entry.get()
        self.expense = self.expense_entry.get()
        self.category = self.category_combo.get()
        self.account = self.account_combo.get()

        balance_list = []
        for self.rows in db.balance_fetch():
            balance_list.append(self.rows)
        self.coin = balance_list[0]  # account id
        self.coin_balance = self.coin[1]
        self.new_balance = int(self.coin_balance - self.amount)
        self.coin_balance = f"{self.coin_balance:,d}"
        self.final_CoinBalance = f"{self.new_balance:,d}"
        #bills
        self.bills = balance_list[1]  # account id
        self.bills_balance = self.bills[1]
        self.new_balance = int(self.bills_balance - self.amount)
        self.bills_balance = f"{self.bills_balance:,d}"
        self.final_BillsBalance = f"{self.new_balance:,d}"
        #mitsi
        self.mitsi = balance_list[5]  # account id
        self.mitsi_balance = self.mitsi[1]
        self.new_balance = int(self.mitsi_balance - self.amount)
        self.mitsi_balance = f"{self.mitsi_balance:,d}"
        self.final_MitsiBalance = f"{self.new_balance:,d}"

        if self.account == "Coin":
            db.expense(self.expense, self.amount, self.account, self.category, self.coin_balance,
                       self.final_CoinBalance, random.randint(1, 10000))
        elif self.account == "Bills":
            db.expense(self.expense, self.amount, self.account, self.category, self.bills_balance,
                       self.final_BillsBalance, random.randint(1, 10000))
        elif self.account == "Mitsubishi":
            db.expense(self.expense, self.amount, self.account, self.category, self.mitsi_balance,
                       self.final_MitsiBalance, random.randint(1, 10000))
        self.refresh_list()
        print(f"Successfully added the data to the expense report Database")
        print(f"Successfully updated the expense category Database")
        self.expenseEntry.delete(0, END)
        self.amountEntry.delete(0, END)
        self.accountCombo.delete(0, END)
        self.categoryCombo.delete(0, END)

    # TODO: Add a remove button to remove from databasee. incase of a mistake expense add

    def refresh_list(self):
        for i in self.expenseTree.get_children():
            self.expenseTree.delete(i)
        self.populateExpenseList()

    def select_item(self, event):
        self.selectItem = self.expenseTree.focus()
        self.my_list = []
        tree = self.expenseTree.item(self.selectItem)
        for k, v in tree.items():
            self.my_list.append(v)
        derp = self.my_list[2]
        yeet = derp[0]
        cars = self.my_list[0]
        print(cars, yeet, derp)


class Pricing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.style = ThemedStyle(self)
        self.style.set_theme('scidblue')
        self.controller = controller
        self.pricing_widgets()
        self.populate_pricing()

        self.button1 = ttk.Button(self, text="< Back", command=lambda: controller.show_frame(HomePage))
        self.button1.place(x=25, y=25)

    def pricing_widgets(self):
        self.price = tk.Label(self, text='')
        self.price.grid(row=0, column=0, pady=10, padx=150)
        self.price.configure(foreground='green')

        self.pricingLabel = tk.Label(self, text='Pricing', font='Arial 30 bold')
        self.pricingLabel.grid(row=1, column=1, pady=10, columnspan=10)
        self.pricingLabel.configure(foreground='green')
        # Tree View
        self.pricingTree = ttk.Treeview(self, height=10, columns=('id', 'title'))
        self.pricingTree.heading('#0', text='Title', anchor=tk.CENTER)
        self.pricingTree.heading('#1', text='Price', anchor=tk.CENTER)
        self.pricingTree.heading('#2', text='id', anchor=tk.CENTER)
        self.pricingTree.column('#0', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.pricingTree.column('#1', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.pricingTree.column('#2', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.pricingTree.grid(row=2, column=1, columnspan=10, pady=15)

        self.pricingTree.bind('<ButtonRelease-1>', self.select_item)

        self.title_entry = tk.StringVar()
        self.titleEntry = ttk.Entry(self, width=10, textvariable=self.title_entry)
        self.titleEntry.grid(row=3, column=1)

        self.cost_entry = tk.IntVar()
        self.costEntry = ttk.Entry(self, width=10, textvariable=self.cost_entry)
        self.costEntry.grid(row=3, column=2, pady=10, padx=25)

        self.updateButton = ttk.Button(self, text="Update", width=20, command=self.update)
        self.updateButton.grid(row=3, column=3, pady=10)

    def populate_pricing(self):
        for row in db.pricingfetch():
            self.pricingTree.insert('', 0, text=row[0], values=(row[1], row[2]))


    def refresh_list(self):
        for i in self.pricingTree.get_children():
            self.pricingTree.delete(i)
        self.populate_pricing()

    def select_item(self, event):
        self.selectItem = self.pricingTree.focus()
        self.my_list = []
        tree = self.pricingTree.item(self.selectItem)
        for k, v in tree.items():
            self.my_list.append(v)
        derp = self.my_list[2]
        yeet = derp[1]
        cars = derp[0]
        # print(derp)
        # print(yeet)
        # print(cars)
        self.titleEntry.delete(0, END)
        self.titleEntry.insert(END, cars)
        self.costEntry.delete(0, END)
        self.costEntry.insert(END, yeet)

    def update(self):
        self.selectItem = self.pricingTree.focus()
        for selected in self.pricingTree.selection():
            data = self.pricingTree.set(selected, '#2')
        item = self.pricingTree.item(self.selectItem)
        values = []
        keys = []
        for k, v in item.items():
            values.append(v)
            keys.append(k)
        data = values[0]
        db.update(self.title_entry.get(), self.cost_entry.get(), data)
        print(f"Successfully updated the price of {self.title_entry.get()} to {self.cost_entry.get()}")
        self.refresh_list()
        self.titleEntry.delete(0, END)
        self.costEntry.delete(0, END)


# TODO: Insert a text thing. so i can add all transactions to a database at end of thr day. like a logger through out the day


if __name__ == "__main__":
    app = Master()
    app.iconbitmap(r'money.ico')
    app.title('My Expense App')
    app.mainloop()
