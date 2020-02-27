import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS report (payee TEXT, fromm TEXT, too TEXT, amount INTEGER, category TEXT, profit INTEGER, id INTEGER PRIMARY KEY)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS pricing (id INTEGER PRIMARY KEY, title TEXT, price INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS positive (category TEXT, profit INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS accounts (account TEXT NOT NULL, balance DECIMAL NOT NULL DEFAULT 0,PRIMARY KEY (account))")
        self.cur.execute("CREATE TABLE IF NOT EXISTS outstanding (payee TEXT PRIMARY KEY, balance INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS expensereport (expense TEXT, amount INTEGER, account TEXT, category TEXT, before_balance TEXT, after_balance TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS expense (expense TEXT PRIMARY KEY, total INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS loans (person TEXT PRIMARY KEY, amount INTEGER)")
        # self.cur.execute("CREATE TABLE IF NOT EXISTS users (user TEXT PRIMARY KEY)")
        # self.cur.execute("CREATE TABLE IF NOT EXISTS passwords (password TEXT PRIMARY KEY)")
        self.conn.commit()


    # def user_fetch(self):
    #     self.cur.execute("SELECT * FROM users")
    #     rows = self.cur.fetchall()
    #     return rows
    #
    # def user_insert(self, user):

    #     self.cur.execute("INSERT INTO users VALUES (?)", (user,))
    #     self.conn.commit()
    #
    # def pass_fetch(self):
    #     self.cur.execute("SELECT * FROM passwords")
    #     rows = self.cur.fetchall()
    #     return rows

    # def pass_insert(self, passw):
    #     self.cur.execute("INSERT INTO passwords VALUES (?)", (passw,))
    #     self.conn.commit()

    def mainfetch(self):
        self.cur.execute("SELECT * FROM accounts")
        rows = self.cur.fetchall()
        return rows

    def loanfetch(self):
        self.cur.execute("SELECT SUM(amount) FROM loans")
        rows = self.cur.fetchall()
        return rows

    def shit_list(self):
        self.cur.execute("SELECT SUM(owing) FROM shitlist")
        sums = self.cur.fetchall()
        return sums

    def pricingfetch(self):
        self.cur.execute("SELECT * FROM pricing")
        rows = self.cur.fetchall()
        return rows

    def re_insert(self, profit, account):
        self.cur.execute("SELECT * FROM accounts")
        self.cur.execute(f"UPDATE accounts SET balance = balance + {profit} WHERE account = '{account}'")
        self.conn.commit()


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

    def account_total(self):
        self.cur.execute("SELECT SUM(balance) FROM accounts")
        sums = self.cur.fetchall()
        return sums

    def expense_total(self):
        self.cur.execute("SELECT SUM(total) FROM expense")
        sums = self.cur.fetchall()
        return sums

    def positive_total(self):
        self.cur.execute("SELECT SUM(balance) FROM positive")
        sums = self.cur.fetchall()
        return sums

    def update(self, title, price, id):
        self.cur.execute("SELECT * FROM pricing")
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
        self.cur.execute(f"UPDATE positive SET balance = balance + {profit} WHERE category = '{categories}'")
        self.conn.commit()

    def balance_fetch(self):
        self.cur.execute("SELECT * FROM accounts")
        rows = self.cur.fetchall()
        return rows

    def expensereport_fetch(self):
        self.cur.execute("SELECT * FROM expensereport")
        rows = self.cur.fetchall()
        return rows

    def positive_fetch(self):
        self.cur.execute("SELECT * FROM positive")
        rows = self.cur.fetchall()
        return rows

    def expense_fetch(self):
        self.cur.execute("SELECT * FROM expense")
        rows = self.cur.fetchall()
        return rows


    def expense(self, expenses, amount, account, category, before_balance, after_balance, id):
        self.cur.execute("SELECT * FROM accounts")
        self.cur.execute("SELECT * FROM expensereport")
        self.cur.execute("SELECT * FROM expense")
        self.cur.execute("INSERT INTO expensereport VALUES (?, ?, ?, ?, ?, ?, ?)", (expenses, amount, account, category, before_balance, after_balance, id))
        self.cur.execute(f"UPDATE expense SET total = total - {amount} WHERE expenses = '{category}'")
        self.cur.execute(f"UPDATE accounts SET balance = balance - {amount} WHERE account = '{account}'")
        self.conn.commit()

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

    def outstanding_transaction(self, account, balance):
        self.cur.execute("SELECT * FROM accounts")
        self.cur.execute(f"UPDATE accounts SET balance = balance + {balance} WHERE account = '{account}'")
        self.cur.execute(f"UPDATE accounts SET balance = balance - {balance} WHERE account = 'Toyota'")
        self.conn.commit()


    def outstanding_paid(self, payee, balance):
        self.cur.execute("SELECT * FROM outstanding")
        person = {people[0] for people in self.cur.fetchall()}
        if payee in person:
            self.cur.execute(f"UPDATE outstanding SET balance = balance - {balance} WHERE payee = '{payee}'")
        else:
            print(f"Error finding {payee} in database")
        self.conn.commit()

    # def outstanding_paid(self, payee, balance):
    #     self.cur.execute("SELECT * FROM outstanding")
    #     rows = self.cur.fetchall()
    #     for x in rows:
    #         person = x[0]
    #         outstanding = x[1]
    #     if payee in person:
    #         self.cur.execute(f"UPDATE outstanding SET balance = balance - {balance} WHERE payee = '{payee}'")
    #     else:
    #         print(f"Error finding {payee} in database")
    #     self.conn.commit()



    # Need to add removing from the database when removing from reports


            
    def __del__(self):
        self.conn.close()
