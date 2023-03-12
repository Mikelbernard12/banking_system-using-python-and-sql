from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
import datetime as lk


DB_NAME = 'AM_bank'
today = lk.datetime.now()
TABLES = {'client': (
    "CREATE TABLE `client` ("
    "  `client_id` int NOT NULL AUTO_INCREMENT,"
    "  `first_name` varchar(60) NOT NULL,"
    "  `last_name` varchar(60) NOT NULL,"
    "  `password`  varchar(255) NOT NULL,"
    "  `Amount` int NOT NULL,"
    "  `date` datetime ,"
    "   PRIMARY KEY(client_id)"
    ") ENGINE=InnoDB")}

my_db = mysql.connector.connect(user="root", passwd="michaelbernard12", database="AM_bank",
                                auth_plugin='mysql_native_password')

my_cursor = my_db.cursor()


def create_database(my_cursors):
    try:
        my_cursors.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as errors:
        print("Failed creating database: {}".format(errors))
        exit(1)


try:
    my_cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as error:
    print("Database {} does not exists.".format(DB_NAME))
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(my_cursor)
        print("Database {} created successfully.".format(DB_NAME))
        my_db.database = DB_NAME
    else:
        print(error)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        my_cursor.execute(table_description)
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(error.msg)
    else:
        print("OK")

add_employee = ("INSERT INTO client "
                "(first_name, last_name, password, Amount, date)"
                "VALUES (%s, %s, %s, %s, %s)")
# add_amt = ("UPDATE client "
#            "set Amount=%s"
#            "where fi")
my_cursor.execute("select * from client")
result = my_cursor.fetchall()


def success(f_name, l_name):
    print("Account for " + f_name + " " + l_name + " successfully created!!!\n"
                                                   "Please keep ur account password safe for next use.")


class Account:

    def __init__(self):
        self.f_name = ""
        self.l_name = ""
        self.password = ""
        self.amt = 0
        self.choice = 0
        self.add = 0

    def create_account(self):
        global today
        #   Create an account which would register login in the database
        self.f_name += input("Enter your first name: ").title()
        self.l_name += input("Enter your last name: ").title()
        self.password += str(input('Enter your password: '))
        self.amt += int(input("Enter an initial deposit: "))
        success(self.f_name, self.l_name)
        data_client = (self.f_name, self.l_name, self.password, self.amt, today)
        my_cursor.execute(add_employee, data_client)
        my_db.commit()

    def withdrawing(self):
        #  Here money is withdrawn from the account if and only if the account exists in the database.
        global result
        f_name = input("Enter your first name: ").title()
        l_name = input("Enter your last name: ").title()
        password = input("Enter your password name: ")
        cunny = 0
        for i in result:
            cunny += 1
            if i[3] == password and i[2] == l_name and i[1] == f_name:
                self.choice = int(input("How much do you want to withdraw: "))
                if i[4] > self.choice:
                    actual_amount = i[4]
                    actual_amount -= self.choice
                    print(f"Amount left: {actual_amount}.0 FCFA.\n Account Id number: {cunny}")
                else:
                    actual_amount = i[4]
                    print(f"insufficient funds.\nAmount left: {actual_amount}.0 FCFA.\nAccount Id number: {cunny} .\n"
                          f"Can't perform any withdrawal.")
        else:
            print("Try again later ....")

    def deposit(self):
        #  Here money is deposited in the account if and only if the account exists in the database.
        global result
        f_name = input("Enter your first name: ").title()
        l_name = input("Enter your last name: ").title()
        password = input("Enter your password name: ")
        id_number = int(input("Enter your bank id number: "))
        couny = 0
        for i in result:
            couny += 1
            if i[3] == password and i[2] == l_name and i[1] == f_name:
                if couny == id_number:
                    new_amount = int(input("Amount to deposit: "))
                    add_amt = ("UPDATE client "
                               "set Amount=%s"
                               f"where client_id= {couny}")

    def balance(self):
        #  This method cross-checks the amount in the account, if and only if the account exists in the database.
        global result
        f_name = input("Enter your first name: ").title()
        l_name = input("Enter your last name: ").title()
        password = input("Enter your password name: ")
        couries = 0
        for i in result:
            couries += 1
            if i[3] == password and i[2] == l_name and i[1] == f_name:
                actual_amount = i[4]
                date_now = i[5]
                num = i[0]
                print(f"{f_name} {l_name}'s account.\n"
                      f"Amount left in this account is : {actual_amount}.0 FCFA.\n"
                      f"Account was valid since {date_now}.\n"
                      f"Account Id Number: {num}.\n"
                      f"Thanks for choosing us...")
            else:
                print("This Account doesn't exist, verify your initials.")
