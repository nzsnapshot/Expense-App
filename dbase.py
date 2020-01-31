import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS list (id INTEGER PRIMARY KEY, category TEXT, quantity INTEGER, price INTEGER, total TEXT)")
        self.conn.commit()

    def mainfetch(self):
        self.cur.execute("SELECT * FROM main")
        rows = self.cur.fetchall()
        return rows

    def pricingfetch(self):
        self.cur.execute("SELECT * FROM pricing")
        rows = self.cur.fetchall()
        return rows

    def reportfetch(self):
        self.cur.execute("SELECT * FROM report")
        rows = self.cur.fetchall()
        return rows

    def insert(self, payee, fromm, to, amount, category, profit, id):
        self.cur.execute("INSERT INTO report VALUES (?, ?, ?, ?, ?, ?, ?)", (payee, fromm, to, amount, category, profit, id))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM list WHERE id=?", (id,))
        self.conn.commit()

    def read_from_db(self):
        self.cur.execute("SELECT SUM(price) FROM list")
        sums = self.cur.fetchall()
        return sums

    def update(self, title, price, id):
        self.cur.execute("UPDATE pricing SET title = ?, price = ? WHERE id = ?", (title, price, id))
        self.conn.commit()

    def transaction(self, amount, accounted, accountz):
        # self.cur.execute("CREATE TABLE accounts (account TEXT NOT NULL, balance DECIMAL NOT NULL DEFAULT 0,PRIMARY KEY (account), CHECK(balance >= 0))")
        self.cur.execute("SELECT * FROM accounts")
        self.cur.execute("BEGIN TRANSACTION")
        self.cur.execute(f"UPDATE accounts SET balance = balance - {amount} WHERE account = '{accounted}'")
        self.cur.execute(f"UPDATE accounts SET balance = balance + {amount} WHERE account = '{accountz}'")
        self.conn.commit()

    def remove_profit(self, amount, category, account):
        self.cur.execute("SELECT * FROM positive")
        self.cur.execute(f"UPDATE positive SET balance = balance - {amount} WHERE category = '{category}'")
        self.cur.execute(f"UPDATE accounts SET balance = balance - {amount} WHERE account = '{account}'")
        self.conn.commit()

    def remove_amount_fromto(self, amount, account):
        self.cur.execute("SELECT * FROM accounts")
        self.cur.execute(f"UPDATE accounts SET balance = balance - {amount} WHERE account = '{account}'")
        self.conn.commit()

    def positive(self, categories, profit):
        self.cur.execute("SELECT * FROM positive")
        # self.cur.execute("INSERT INTO positive VALUES (?, ?)", (category, profit))
        self.cur.execute(f"UPDATE positive SET balance = balance + {profit} WHERE category = '{categories}'")
        self.conn.commit()
        # self.cur.execute("INSERT INTO report VALUES (?, ?, ?, ?, ?, ?)", ( payee, fromm, to, amount, category, profit))

    def transactionFetch(self):
        self.cur.execute("SELECT * FROM accounts")
        rows = self.cur.fetchall()
        return rows

    def removeReport(self):
        self.cur.execute("SELECT ")

    def outstanding_insert(self, payee, balance):
        self.cur.execute("SELECT payee FROM outstanding")
        person = {people[0] for people in self.cur.fetchall()}
        if payee in person:
            print('Works')
            self.cur.execute(f"UPDATE outstanding SET balance = balance + {balance} WHERE payee = '{payee}'")
        else:
            self.cur.execute(f"INSERT INTO outstanding VALUES (?, ?)",  (payee, balance))
        self.conn.commit()

    def outstanding_fetch(self):
        self.cur.execute("SELECT * FROM outstanding")
        rows = self.cur.fetchall()
        return rows



    def outstanding_paid(self):
        self.cur.execute("SELECT")


    # Need to add removing from the database when removing from reports


            
    def __del__(self):
        self.conn.close()
