from new_account import Account

# my_db = mysql.connector.connect(user="root", passwd="michaelbernard12", database="AM_bank",
#                                 auth_plugin='mysql_native_password')
#
# my_cursors = my_db.cursor()

account = Account()


print("Welcome to AM_bank ,our services are as follows:\n"
      "----- a.Create an account-----\n"
      "----- b.Withdraw Money-----\n"
      "----- c.Deposit Money-----\n"
      "----- d.Client Balance-----\n"
      "----- e.Quit-----\n"
      "Enter the corresponding letters to the services.\n"
      "Thanks for understanding\n")
client_choice = input("Enter your choice: ").lower()
if client_choice == "a":
    account.create_account()
    # account.checking_credentials(account.create_account())
elif client_choice == "b":
    account.withdrawing()
elif client_choice == "c":
    account.deposit()
elif client_choice == "d":
    account.balance()
elif client_choice == "e":
    print("Thanks for choosing our Banking system.\n"
          "See you next time.")
