# Simple Banking System

This is a simple banking system that allows users to:
- Create an account (card number and PIN are automatically generated)
- Log into account
- Check account balance
- Deposit money
- Do transfer to another account
- Close account

The program uses the `sqlite3 module` to manage SQLite database.
All data are stored in `card.s3db` file which is created when the program is first started.

## Get started
- download the repository
- run the program in the command-line
```
SimpleBankingSystem > python main.py
```
### Sample usage
```
1. Create an account
2. Log into account
0. Exit
1
Your card has been created
Your card number:
4000008215809778
Your card PIN:
3321

1. Create an account
2. Log into account
0. Exit
2
Enter your card number:
4000008215809778
Enter your PIN:
3321
You have successfully logged in!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
2
Enter income:
3750
Income was added!
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
1
Balance: 3750
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
5
You have successfully logged out!
```
```
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
3
Enter card number:
4000008215809778
You can't transfer money to the same account!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
3
Enter card number:
4000009122239497
Enter how much money you want to transfer: 30000
Not enough money!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
3
Enter card number:
4000009122239497
Enter how much money you want to transfer: 2000
Success!
```
