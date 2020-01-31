import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox
from dbase import Database
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
import decimal
import logging
import sys
import os
import random
import sqlite3
db = Database('saved.db')

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

    
class Master(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.style = ThemedStyle(self)
        self.style.set_theme('scidblue')

        for F in (HomePage, Sales, Owing, Summary, Expense, Pricing):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=1, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.style = ThemedStyle(self)
        self.style.set_theme('scidblue')
        self.controller = controller
        self.create_widgets()
        self.populate_list()

        # self.imgtitle = ImageTk.PhotoImage(Image.open(resource_path('slems.png')))
        # self.lab = tk.Label(self, image=self.imgtitle)
        # self.lab.place(x=150,y=300)

        label = tk.Label(self, text="Expense App", font=('Arial 30 bold'))
        label.configure(foreground='green')
        label.grid(row=0, column=0, columnspan=5, pady=10)

        button = ttk.Button(self, text="Sales", width=15, command=lambda: controller.show_frame(Sales))
        button.grid(row=1, column=0, padx=25, pady=25)
 
        button2 = ttk.Button(self, text="Owing", width=15,command=lambda: controller.show_frame(Owing))
        button2.grid(row=1, column=1, padx=25, pady=25)

        button3 = ttk.Button(self, text="Summary", width=15, command=lambda: controller.show_frame(Summary))
        button3.grid(row=1, column=2, padx=25, pady=25)

        button4 = ttk.Button(self, text="Expense", width=15, command=lambda: controller.show_frame(Expense))
        button4.grid(row=2, column=0, padx=25, pady=25)
        
        button4 = ttk.Button(self, text="Pricing", width=15, command=lambda: controller.show_frame(Pricing))
        button4.grid(row=2, column=1, padx=25, pady=25)
        ttk.Button(self, text="Restart", command=restart_program).grid(row=2, column=2)


    
    
    def create_widgets(self):
        # Tree View
        self.balanceTree = ttk.Treeview(self, height=10, columns=('id'))
        self.balanceTree.heading('#0', text='Account', anchor=tk.CENTER)
        self.balanceTree.heading('#1', text='Current', anchor=tk.CENTER)
        self.balanceTree.column('#0', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.balanceTree.column('#1', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.balanceTree.grid(row=3, column=0, columnspan=3, pady=15)


    def populate_list(self):
        for main in db.transactionFetch():
            self.balanceTree.insert('', 0, text=main[0], values=main[1])


class Sales(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.style = ThemedStyle(self)
        self.style.set_theme('scidblue')
        self.controller = controller
        self.create_widgets()
        self.refresh()
        # self.populateReportList()

        self.transaction_accounts = []
        self.transaction_balances = []
        for k, v in db.transactionFetch():
            self.transaction_accounts.append(k)
            self.transaction_balances.append(v)
        self.mitsubishi = self.transaction_accounts[0]
        self.coin = self.transaction_accounts[1]
        self.bills = self.transaction_accounts[2]
        self.toyota = self.transaction_accounts[3]
        self.mazdas = self.transaction_accounts[4]
        self.citeron = self.transaction_accounts[5]
        self.oranges = self.transaction_accounts[6]

        self.mitsubishiBalance = self.transaction_balances[0]
        self.coinBalance = self.transaction_balances[1]
        self.billsBalance = self.transaction_balances[2]
        self.toyotaBalance = self.transaction_balances[3]
        self.mazdasBalance = self.transaction_balances[4]
        self.citeronBalance = self.transaction_balances[5]
        self.orangesBalance = self.transaction_balances[6]

        self.listed = []

        self.button1 = ttk.Button(self, text="<", command=lambda: controller.show_frame(HomePage))
        self.button1.place(x=15,y=15)

    def create_widgets(self):
        self.value, self.coin = [], [] 
        for x in db.mainfetch():
            self.value.append(x[0])
            self.coin.append(x[1])
           
        self.category_values = ['Business','Personal Profits', 'Round Up', 'Oranges', 'Bonus', 'Others']
        self.titleLabel = tk.Label(self, text='Sales', font=('Arial 30 bold'))
        self.titleLabel.grid(row=0, column=0, pady=10, columnspan=7)
        self.titleLabel.configure(foreground='green')

        # Person Label/Title
        self.personsLabel = tk.Label(self, text='Payee', font=('Arial 10 bold'))
        self.personsLabel.grid(row=1, column=0, padx=25)
        # Persons Input Box, Could put a auto complete box after we get a list.
        self.persons_entry = tk.StringVar()
        self.personEntry = ttk.Entry(self, width=15, textvariable='persons_entry')
        self.personEntry.grid(row=2, column=0, pady=10, padx=25)

        # from Label/Title
        self.from_label = tk.Label(self, text='From', font=('Arial 10 bold'))
        self.from_label.grid(row=1, column=1)
        # from dropdown box and selection
        self.from_combo = tk.StringVar()
        self.fromCombo = ttk.Combobox(self, width=10, values=self.value, textvariable=self.from_combo)
        # self.fromCombo.bind('<<ComboboxSelected>>', self.currentBalanceLabels)
        self.fromCombo.grid(row=2, column=1, pady=10, padx=25)

        # To Label/Title
        self.to_label = tk.Label(self, text='To', font=('Arial 10 bold'))
        self.to_label.grid(row=1, column=2)
        # To dropdown box and selection
        self.to_combo = tk.StringVar()
        self.toCombo = ttk.Combobox(self, width=10, values=self.value, textvariable=self.to_combo)
        self.toCombo.grid(row=2, column=2, pady=10, padx=25)

        # Amount Label/Title
        self.amount_label = tk.Label(self, text='Amount', font=('Arial 10 bold'))
        self.amount_label.grid(row=1, column=3)
        # To dropdown box and selection
        self.amount_entry = tk.IntVar()
        self.amountEntry = ttk.Entry(self, width=10, textvariable=self.amount_entry)
        self.amountEntry.grid(row=2, column=3, pady=10, padx=25)

        # To Label/Title
        self.profit_label = tk.Label(self, text='Profit', font=('Arial 10 bold'))
        self.profit_label.grid(row=1, column=4)
        # To dropdown box and selection
        self.profit_entry = tk.StringVar()
        self.profitEntry = ttk.Entry(self, width=10, textvariable=self.profit_entry)
        # self.toCombo.bind('<<ComboboxSelected>>', self.afterBalanceLabels)
        self.profitEntry.grid(row=2, column=4, pady=10, padx=25)

        # To Label/Title
        self.category_label = tk.Label(self, text='Category', font=('Arial 10 bold'))
        self.category_label.grid(row=1, column=5)
        # To dropdown box and selection
        self.category_combo = tk.StringVar()
        self.categoryCombo = ttk.Combobox(self, width=10, values=self.category_values, textvariable=self.category_combo)
        self.categoryCombo.grid(row=2, column=5, pady=10, padx=25)
        
        # Enter Button
        self.enterButton = ttk.Button(self, width=10, text='Enter', command=self.insert)
        self.enterButton.grid(row=5, column=0)

        # Refresh Button
        self.refreshButton = ttk.Button(self, width=10, text='Refresh', command=self.refresh)
        self.refreshButton.grid(row=4, column=0)

        # Remove Button
        self.removeButton = ttk.Button(self, width=10, text='Remove', command=self.remove)
        self.removeButton.grid(row=6, column=0)

        # Mitsi Entry
        self.mitsi_entry = tk.DoubleVar()
        self.mitsiEntry = ttk.Entry(self, width=10, textvariable=self.mitsi_entry)
        self.mitsiEntry.grid(row=3, column=1)

        # Tree View
        self.tree = ttk.Treeview(self, height=20, columns=('id', 'items', 'total', 'quantity', 'category' ))
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
        self.tree.column('#5', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.tree.grid(row=4, column=1, columnspan=10, padx=20, pady=20, rowspan=5)
        self.tree.bind('<ButtonRelease-1>', self.select_item)

    def populateReportList(self):
        for self.row in db.reportfetch():
            self.tree.insert('', 0, text=self.row[0], values=(self.row[1], self.row[2], self.row[3], self.row[4], self.row[5], self.row[6]))
                                        # Payeee                #from       #to             #amount     #profit       #category     #id


    def deleteallItem(self):
        confirmed = tk.messagebox.askyesno('Please Confirm','Do you want to delete all?')
        # you forgot to add the : at the end of the if statement. You were then calling this function. Which didn't delete anything
        # I made a function that deletes everything if confirmed == True:
        if confirmed == True:
            self.remove()
        elif confirmed == False:
            print('Ok')
    def remove(self):
        confirmed = tk.messagebox.askyesno('Please Confirm','Do you want to delete this item?')
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
                self.cur.execute("DELETE FROM report WHERE id=?", (self.derp,))
                self.conn.commit()
            
            self.conn.close()
            for i in self.tree.get_children():
                self.tree.delete(i)
            self.populateReportList()
        elif confirmed == False:
            print('Ok')

    def refresh(self):
        value, price = [], []
        for x in db.pricingfetch():
            value.append(x[0])
            price.append(x[1])
        mitsi, oranges, citeron, mazda = price[0], price[1], price[2], price[3]
        if self.from_combo.get() == "Mitsubishi":
            self.dollars = int(self.mitsi_entry.get() * mitsi)
            self.amount = self.amount_entry.get()
            amounts = self.amount - self.dollars
            self.profitEntry.delete(0, END)
            self.profitEntry.insert(END, amounts)
        elif self.from_combo.get() == "Oranges":
            self.dollars = int(self.mitsi_entry.get() * oranges)
            self.amount = self.amount_entry.get()
            amounts = self.amount - self.dollars
            self.profitEntry.delete(0, END)
            self.profitEntry.insert(END, amounts)
        elif self.from_combo.get() == "Mazdas":
            self.dollars = int(self.mitsi_entry.get() * mazda)
            self.amount = self.amount_entry.get()
            amounts = self.amount - self.dollars
            self.profitEntry.delete(0, END)
            self.profitEntry.insert(END, amounts)
        elif self.from_combo.get() == "Citeron":
            self.dollars = int(self.mitsi_entry.get() * citeron)
            self.amount = self.amount_entry.get()
            amounts = self.amount - self.dollars
            self.profitEntry.delete(0, END)
            self.profitEntry.insert(END, amounts)
        self.refresh_list()

    def refresh_list(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.populateReportList()

    def insert_into_table(self):
        payee = self.personEntry.get()
        fromm = self.from_combo.get()
        to = self.to_combo.get()
        amount = self.amount_entry.get()
        profit = self.profit_entry.get()
        category = self.category_combo.get()
        db.transaction(amount, fromm, to)
        db.positive(category, profit)
        db.insert(payee, fromm, to, amount, profit, category, random.randint(1, 10000))
        print(f"Successfully transfered from accounts {fromm} to {to} ")
        print(f"Successfully added {profit} to the account {to}")
       

    def insert(self):
        try:
            payee = self.personEntry.get()
            fromm = self.from_combo.get()
            to = self.to_combo.get()
            amount = self.amount_entry.get()
            profit = self.profit_entry.get()
            category = self.category_combo.get()
            lst = [payee, fromm, to, amount, category]
            # for self.x in lst:
            #     if self.x == '':
            #         messagebox.showinfo("Title", f"You cannot have blank entry boxes")
            #         restart_program()
            if to == 'Toyota':
                self.insert_into_table()
                db.outstanding_insert(payee, amount)
                print(f"Successfully added to {payee}'s oustanding balance. ")
                self.refresh_list()
            else:
                try:
                    self.insert_into_table()
                    # self.personEntry.delete(0, END)
                    # self.profitEntry.delete(0, END)
                    # self.fromCombo.delete(0, END)
                    # self.toCombo.delete(0, END)
                    # self.amountEntry.delete(0, END)
                    # self.categoryCombo.delete(0, END)
                except sqlite3.IntegrityError:
                    print(f"Please restart the programme, you tried to transfer an amount more than what is in there")
                self.refresh_list()
        except sqlite3.OperationalError:
                print("Error please restart programme")


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
        tk.Frame.__init__(self,parent)
        self.style = ThemedStyle(self)
        self.style.set_theme('scidblue')
        self.controller = controller
        self.owing_widgets()
        self.populate_owing()

        self.button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        self.button1.place(x=25,y=25)

    def owing_widgets(self):
        # Owing Label
        self.ticklistLabel = tk.Label(self, text='Outstanding', font=('Arial 30 bold'))
        self.ticklistLabel.grid(row=0, column=0, pady=10, columnspan=10)
        self.ticklistLabel.configure(foreground='green')
        # Outstanding Button

        self.payeeLabel = tk.Label(self, text='Payee', font=('Arial 10 bold'))
        self.payeeLabel.grid(row=2, column=1)
        self.outstandingLabel = tk.Label(self, text='Outstanding', font=('Arial 10 bold'))
        self.outstandingLabel.grid(row=2, column=2)
        self.payingLabel = tk.Label(self, text='Paying', font=('Arial 10 bold'))
        self.payingLabel.grid(row=2, column=3)

        self.paidButton = ttk.Button(self, width=10, text='Paid', command="")
        self.paidButton.grid(row=3, column=4, pady=25)

        self.payee_entry = tk.StringVar()
        self.payeeEntry = ttk.Entry(self, width=10, textvariable=self.payee_entry)
        self.payeeEntry.grid(row=3, column=1, pady=25)

        self.payee_entry = tk.StringVar()
        self.payeeEntry = ttk.Entry(self, width=10, textvariable=self.payee_entry)
        self.payeeEntry.grid(row=3, column=3, pady=25)


        self.balance_entry = tk.IntVar()
        self.balanceEntry = ttk.Entry(self, width=10, textvariable=self.balance_entry)
        self.balanceEntry.grid(row=3, column=2, pady=25)

        # Tree View
        self.owingTree = ttk.Treeview(self, height=10, columns=('outstanding'))
        self.owingTree.heading('#0', text='Payee', anchor=tk.CENTER)
        self.owingTree.heading('#1', text='Balance', anchor=tk.CENTER)
        self.owingTree.column('#0', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.owingTree.column('#1', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.owingTree.grid(row=1, column=0, columnspan=5, padx=150, pady=15)

        self.owingTree.bind('<ButtonRelease-1>', self.select_item)

    def populate_owing(self):
        for self.row in db.outstanding_fetch():
            self.owingTree.insert('', 0, text=self.row[0], values=self.row[1])


    def select_item(self, event):
        self.selectItem = self.owingTree.focus()
        self.my_list = []
        tree = self.owingTree.item(self.selectItem)
        for k, v in tree.items():
            self.my_list.append(v)
        derp = self.my_list[2]
        yeet = derp[0]
        cars = self.my_list[0]



class Summary(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.style = ThemedStyle(self)
        self.style.set_theme('scidblue')
        
        self.controller = controller
        self.button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        self.button1.place(x=25,y=25)


class Expense(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.style = ThemedStyle(self)
        self.style.set_theme('scidblue')
        self.controller = controller

        self.button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        self.button1.place(x=25,y=25)



class Pricing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.style = ThemedStyle(self)
        self.style.set_theme('scidblue')
        self.controller = controller
        self.pricing_widgets()
        self.populate_pricing()

        self.button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        self.button1.place(x=25,y=25)

    def pricing_widgets(self):
        self.pricingLabel = tk.Label(self, text='Pricing', font=('Arial 30 bold'))
        self.pricingLabel.grid(row=0, column=0, pady=10, columnspan=10)
        self.pricingLabel.configure(foreground='green')
        # Tree View
        self.pricingTree = ttk.Treeview(self, height=10, columns=('id', 'title'))
        self.pricingTree.heading('#0', text='Title', anchor=tk.CENTER)
        self.pricingTree.heading('#1', text='Price', anchor=tk.CENTER)
        self.pricingTree.heading('#2', text='id', anchor=tk.CENTER)
        self.pricingTree.column('#0', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.pricingTree.column('#1', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.pricingTree.column('#2', stretch=tk.YES, minwidth=50, width=100, anchor='center')
        self.pricingTree.grid(row=1, column=0, columnspan=5, padx=300, pady=15)

        self.pricingTree.bind('<ButtonRelease-1>', self.select_item)

        self.cars_entry = tk.StringVar()
        self.carsEntry = ttk.Entry(self, width=20, textvariable=self.cars_entry)
        self.carsEntry.place(x=450, y=328)
  
        self.cost_entry = tk.IntVar()
        self.costEntry = ttk.Entry(self, width=20, textvariable=self.cost_entry)
        self.costEntry.grid(row=2, column=0, padx=275)

        self.updateButton = ttk.Button(self, text="Update", width=20, command=self.update)
        self.updateButton.grid(row=3, column=0, pady=10, padx=275)

    def populate_pricing(self):
        for row in db.pricingfetch():
            self.pricingTree.insert('', 0, text=row[0], values=(row[1], row[2]))

    def select_item(self, event):
        self.selectItem = self.pricingTree.focus()
        self.my_list = []
        tree = self.pricingTree.item(self.selectItem)
        for k, v in tree.items():
            self.my_list.append(v)
        derp = self.my_list[2]
        yeet = derp[0]
        cars = self.my_list[0]
        self.carsEntry.delete(0, END)
        self.carsEntry.insert(END, cars)
        self.costEntry.delete(0, END)
        self.costEntry.insert(END, yeet)

    def update(self):
        self.selectItem = self.pricingTree.focus()
        for selected in self.pricingTree.selection():
            data = self.pricingTree.set(selected, '#2')
        item = self.pricingTree.item(self.selectItem)
        db.update(self.cars_entry.get(), self.cost_entry.get(), data)
        for i in self.pricingTree.get_children():
            self.pricingTree.delete(i)
        self.populate_pricing()
        self.carsEntry.delete(0, END)
        self.costEntry.delete(0, END)




if __name__ == "__main__":
    app = Master()
    app.iconbitmap(r'money.ico')
    app.title('My Expense App')
    app.mainloop()


