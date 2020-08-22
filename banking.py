import random
import sqlite3


class UserMenu:

    def __init__(self):
        self.logged = False
        self.loaded_account_data = 0
        self.turn_off = False
        self.iin = ['4', '0', '0', '0', '0', '0']
        self.main_interface_message = "\n1. Create an account \n2. Log into account \n0. Exit "
        self.account_interface_message = "\n1. Balance \n2. Add income \n3. Do transfer " \
                                         "\n4. Close account \n5. Log out \n0. Exit "
        # Prepare database
        self.connection = sqlite3.connect("card.s3db")
        self.cur = self.connection.cursor()
        try:
            self.sql_command = """CREATE TABLE card(  
                            id INTEGER,
                            number TEXT,
                            pin TEXT,
                            balance INTEGER DEFAULT 0
                            );"""
            self.cur.execute(self.sql_command)
            self.sql_command = "INSERT INTO card VALUES (0, 1111, 2222, 1508);"
            self.cur.execute(self.sql_command)
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def __str__(self):
        self.sql_command = """SELECT * FROM card"""
        self.cur.execute(self.sql_command)
        self.cur.fetchall()
        return " ".join(self.cur.fetchall())

    def main_interface(self):
        while not self.turn_off:
            if self.logged:
                print(self.account_interface_message)
                user_action = int(input("> "))
                while True:
                    self.account_action(user_action)
                    if not self.logged:
                        break
                    if self.turn_off:
                        break
                    print(self.account_interface_message)
                    user_action = int(input("> "))

            elif not self.logged:
                print(self.main_interface_message)
                user_action = int(input("> "))
                while True:
                    self.start_action(user_action)
                    if self.logged:
                        break
                    if self.turn_off:
                        break
                    print(self.main_interface_message)
                    user_action = int(input("> "))
        self.connection.close()
        return

    def start_action(self, select):

        if select == 0:  # Turn off
            self.turn_off = True

        elif select == 1:  # Make a new account number
            account_number = ''.join(self.iin)
            for _i in range(9):
                account_number += str(random.randint(0, 9))
            account_number += self.luhn_algorithm(account_number)  # Use Luhn algorithm to find last digit
            pin = str(random.randint(1, 9))  # First number of pin can't be "0", because SQL will drop it!
            for _i in range(3):
                pin += str(random.randint(0, 9))
            self.sql_command = f"INSERT INTO card VALUES (0, {account_number}, {pin}, 0)"
            self.cur.execute(self.sql_command)
            self.connection.commit()
            print("\nYour card has been created! \nYour card number: \n{} \nYour card PIN: \n{}"
                  .format(account_number, pin))
            return

        elif select == 2:  # Log into account
            print("\nEnter your card number:")
            user_card_number = input("> ")
            print("Enter your PIN:")
            user_pin = input("> ")
            # Load account data if account number and pin is correct
            self.sql_command = f"SELECT id, number, pin, balance " \
                               f"FROM card " \
                               f"WHERE number = {user_card_number} AND pin = {user_pin};"
            self.cur.execute(self.sql_command)
            self.loaded_account_data = self.cur.fetchone()
            if self.loaded_account_data:  # Check if any account is loaded, if True, it is selected one
                self.logged = True
                self.loaded_account_data = list(self.loaded_account_data)
                print("You have successfully logged in!")
                return
            else:
                print("Wrong card number or PIN!")

        elif select == 3:  # Check all accounts - debug purpose
            self.sql_command = """SELECT * FROM card"""
            self.cur.execute(self.sql_command)
            database = self.cur.fetchall()
            print("\n")
            print("ID | Account Number | PIN | Balance")
            for i in range(0, len(database)):
                print(database[i][0], "|", database[i][1], "|", database[i][2], "|", database[i][3])
        return

    def account_action(self, select):
        if select == 0:  # Turn off
            self.loaded_account_data = 0
            self.logged = False
            self.turn_off = True

        elif select == 1:  # Balance
            print(f"\nBalance: {self.loaded_account_data[3]}")

        elif select == 2:  # Add income
            print("\nEnter income:")
            income = int(input("> "))
            self.loaded_account_data[3] += income
            self.update_account_data("update")
            print("Income was added!")

        elif select == 3:  # Do transfer
            print("\nTransfer")
            print("Enter card number:")
            recipient_account_number = input("> ")
            if recipient_account_number == self.loaded_account_data[1]:
                print("You can't transfer money to the same account!")
            elif len(recipient_account_number) == 16 and \
                    (recipient_account_number[-1] == self.luhn_algorithm(recipient_account_number[:-1])):
                connection2 = sqlite3.connect("card.s3db")
                cur2 = connection2.cursor()
                sql_command = f"SELECT id, number, pin, balance " \
                              f"FROM card " \
                              f"WHERE number = {recipient_account_number};"
                cur2.execute(sql_command)
                loaded_account_data = cur2.fetchone()
                if loaded_account_data:
                    print("Enter how much money you want to transfer: ")
                    money_to_transfer = int(input("> "))
                    if money_to_transfer <= self.loaded_account_data[3]:
                        self.money_transfer(recipient_account_number, money_to_transfer)
                        self.loaded_account_data[3] -= money_to_transfer
                        self.update_account_data("update")
                    else:
                        print("Not enough money!")
                else:
                    print("Such a card does not exist.")
            else:
                print("Probably you made mistake in the card number. Please try again!")

        elif select == 4:  # Close account
            self.update_account_data("delete")
            self.loaded_account_data = 0
            self.logged = False
            print("\nThe account has been closed!")

        elif select == 5:   # Log out
            self.loaded_account_data = 0
            self.logged = False
        return

    def money_transfer(self, account_number, money):
        connection2 = sqlite3.connect("card.s3db")
        cur2 = connection2.cursor()
        sql_command = f"SELECT id, number, pin, balance " \
                      f"FROM card " \
                      f"WHERE number = {account_number};"
        cur2.execute(sql_command)
        loaded_account_data = cur2.fetchone()
        loaded_account_data = list(loaded_account_data)
        loaded_account_data[3] = money + loaded_account_data[3]
        sql_command = f"DELETE FROM card "\
                      f"WHERE number = {account_number};"
        cur2.execute(sql_command)
        sql_command = f"INSERT INTO card " \
                      f"VALUES " \
                      f"(0, " \
                      f"{loaded_account_data[1]}, " \
                      f"{loaded_account_data[2]}, " \
                      f"{loaded_account_data[3]})"
        cur2.execute(sql_command)
        connection2.commit()

    def update_account_data(self, action):
        if action == "update":
            self.sql_command = f"DELETE FROM card " \
                               f"WHERE number = {self.loaded_account_data[1]};"
            self.cur.execute(self.sql_command)
            self.sql_command = f"INSERT INTO card " \
                               f"VALUES " \
                               f"(0, " \
                               f"{self.loaded_account_data[1]}, " \
                               f"{self.loaded_account_data[2]}, " \
                               f"{self.loaded_account_data[3]})"
            self.cur.execute(self.sql_command)
            self.connection.commit()
        elif action == "delete":
            self.sql_command = f"DELETE FROM card " \
                               f"WHERE number = {self.loaded_account_data[1]};"
            self.cur.execute(self.sql_command)
            self.connection.commit()

    def luhn_algorithm(self, number):
        check_sum = 0
        for i in range(len(number)):
            if (i + 1) % 2:
                value = int(number[i]) * 2
                if value > 9:
                    check_sum += value - 9
                else:
                    check_sum += value
            else:
                value = int(number[i])
                if value > 9:
                    check_sum += value - 9
                else:
                    check_sum += value
        if check_sum % 10:
            return str(10 - (check_sum % 10))
        else:
            return '0'


bank_system = UserMenu()
bank_system.main_interface()
