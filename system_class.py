import random
import luhn
import sqlite3
from urllib.request import pathname2url

ERROR = 'Wrong input!\n'


class System:
    def __init__(self, db_name='card.s3db'):
        self.db_name = db_name
        self.conn = None
        self.cur = None
        self.user_cards = {}
        self.currently_logged = None
        self.create_database(db_name)

    def log_in(self):
        card: str = input('Enter your card number: \n')[0:16]
        pin = input('Enter your PIN:\n')
        self.cur.execute(f'SELECT pin FROM card WHERE number = "{card}"')
        try:
            if self.cur.fetchone()[0] == pin:
                self.currently_logged = card
                print('You have successfully logged in!\n')
            else:
                print('Wrong card number or PIN!\n')
        except TypeError:
            print(ERROR)

    def log_out(self):
        self.currently_logged = None
        print('You have successfully logged out!\n')

    def create_new_user(self):
        new_card = self.generate_unique_card_nr()
        new_pin = self.generate_new_pin()
        self.cur.execute(f'INSERT INTO card (number, pin) '
                         f'VALUES("{new_card}", "{new_pin}")')
        self.conn.commit()
        print('Your card has been created\n'
              'Your card number:\n'
              f'{new_card}\n'
              f'Your card PIN:\n'
              f'{new_pin}\n')

    def generate_unique_card_nr(self):
        while True:
            new_nr = "400000" + format(random.randint(000000000, 999999999), '09d')
            new_nr = new_nr + luhn.calculate_reminder(new_nr)
            self.cur.execute(f'SELECT number '
                             f'FROM card '
                             f'WHERE number = {new_nr}')
            if self.cur.fetchone() is None:
                return new_nr

    @staticmethod
    def generate_new_pin():
        return format(random.randint(0000, 9999), '04d')

    def create_database(self, db_name: str):
        try:
            db_uri = 'file:{}?mode=rw'.format(pathname2url(db_name))
            self.conn = sqlite3.connect(db_uri, uri=True)
        except sqlite3.OperationalError:
            # handle missing database case
            self.conn = sqlite3.connect(db_name)
            self.cur = self.conn.cursor()
            self.cur.execute('CREATE TABLE card ('
                             'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                             'number TEXT UNIQUE,'
                             'pin TEXT,'
                             'balance INTEGER DEFAULT 0)')
            self.conn.commit()
        finally:
            self.cur = self.conn.cursor()

    def show_all_records(self):
        for row in self.cur.execute('SELECT * '
                                    'FROM card'):
            print(row)

    def get_balance(self):
        if self.currently_logged is None:
            return
        else:
            self.cur.execute(f'SELECT balance '
                             f'FROM card '
                             f'WHERE number = "{self.currently_logged}"')
        balance = self.cur.fetchone()[0]
        print(f'Balance: {balance}')
        return balance

    def add_income(self):
        try:
            deposit = int(input('Enter income:\n'))
        except ValueError:
            print(ERROR)
        else:
            self.cur.execute(f'UPDATE card '
                             f'SET balance = balance + {deposit} '
                             f'WHERE number = "{self.currently_logged}"')
            self.conn.commit()
            print('Income was added!')

    def check_card(self, target_card):
        try:
            if not luhn.check_number(target_card):
                print('Probably you made a mistake in the card number. Please try again!')
                return False
        except ValueError:
            print(ERROR)
            return False
        else:
            self.cur.execute(f'SELECT number '
                             f'FROM card '
                             f'WHERE number = "{target_card}"')
            card = self.cur.fetchone()
            if card is None:
                print('Such a card does not exist.')
                return False
            elif card[0] == self.currently_logged:
                print("You can't transfer money to the same account!")
                return False
            else:
                return True

    def check_if_balance_sufficient(self, amount):

        self.cur.execute(f'SELECT balance '
                         f'FROM card '
                         f'WHERE number = "{self.currently_logged}"')
        return self.cur.fetchone()[0] > amount

    def do_transfer(self):
        target_card = input('Enter card number:\n')
        if self.check_card(target_card):
            try:
                amount = int(input('Enter how much money you want to transfer:'))
            except ValueError:
                print(ERROR)
            else:
                if self.check_if_balance_sufficient(amount):
                    self.cur.execute(f'UPDATE card '
                                     f'SET balance = balance - {amount} '
                                     f'WHERE number = "{self.currently_logged}"')
                    self.conn.commit()
                    self.cur.execute(f'UPDATE card '
                                     f'SET balance = balance + {amount} '
                                     f'WHERE number = "{target_card}"')
                    self.conn.commit()
                    print('Success!')
                else:
                    print('Not enough money!')

    def close_account(self):
        self.cur.execute(f'DELETE FROM card '
                         f'WHERE number = "{self.currently_logged}"')
        self.conn.commit()
        print('The account has been closed!')
