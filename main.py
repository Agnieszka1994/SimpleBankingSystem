from system_class import *
import os

system = System()
while True:
    while system.currently_logged is None:
        os.system('cls')
        print('1. Create an account')
        print('2. Log into account')
        print('0. Exit')
        try:
            choice = int(input())
        except ValueError:
            print('Integer expected')
        else:
            if choice == 1:
                system.create_new_user()
            elif choice == 2:
                system.log_in()
            elif choice == 0:
                print('Bye')
                exit(0)

    while system.currently_logged is not None:
        os.system('cls')
        print('1. Balance')
        print('2. Add income')
        print('3. Do transfer')
        print('4. Close account')
        print('5. Log out')
        print('0. Exit')
        try:
            choice = int(input())
        except ValueError:
            print('Integer expected')
        else:
            if choice == 1:
                system.get_balance()
            elif choice == 2:
                system.add_income()
            elif choice == 3:
                system.do_transfer()
            elif choice == 4:
                system.close_account()
            elif choice == 5:
                system.log_out()
            elif choice == 0:
                print('Bye')
                exit(0)
