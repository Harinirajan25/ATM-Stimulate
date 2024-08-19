#!/usr/bin/python
import getpass
import os

# creating lists of users, their PINs, and bank statements
users = ['user1', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]

def create_account():
    while True:
        new_user = input('ENTER NEW USERNAME: ').lower()
        if new_user in users:
            print('USERNAME ALREADY EXISTS. TRY AGAIN.')
        else:
            break

    while True:
        new_pin = str(getpass.getpass('CREATE A NEW PIN: '))
        if new_pin.isdigit() and len(new_pin) == 4:
            confirm_pin = str(getpass.getpass('CONFIRM NEW PIN: '))
            if confirm_pin == new_pin:
                break
            else:
                print('PIN MISMATCH. TRY AGAIN.')
        else:
            print('PIN MUST CONSIST OF 4 DIGITS.')

    initial_deposit = int(input('ENTER INITIAL DEPOSIT AMOUNT: '))
    users.append(new_user)
    pins.append(new_pin)
    amounts.append(initial_deposit)

    print('ACCOUNT CREATED SUCCESSFULLY!')
    print('YOU CAN NOW LOGIN WITH YOUR NEW CREDENTIALS.\n')

def login():
    count = 0
    while True:
        user = input('\nENTER USER NAME: ').lower()
        if user in users:
            n = users.index(user)
            break
        else:
            print('INVALID USERNAME')

    # comparing pin
    while count < 3:
        pin = str(getpass.getpass('PLEASE ENTER PIN: '))
        if pin == pins[n]:
            break
        else:
            count += 1
            print('INVALID PIN')

    if count == 3:
        print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING. YOUR CARD HAS BEEN LOCKED.')
        exit()

    print('LOGIN SUCCESSFUL, CONTINUE\n')
    return n

while True:
    print('WELCOME TO THE ATM SYSTEM')
    print('1. LOGIN')
    print('2. CREATE NEW ACCOUNT')
    choice = input('SELECT AN OPTION (1 or 2): ')

    if choice == '1':
        n = login()
        break
    elif choice == '2':
        create_account()
    else:
        print('INVALID OPTION. PLEASE SELECT 1 OR 2.')

# Main menu
while True:
    response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nDeposit____(D) \nChange PIN_(P) \nQuit_______(Q) \n: ').lower()
    if response == 's':
        print(f'{users[n].capitalize()} YOU HAVE {amounts[n]} RUPEES ON YOUR ACCOUNT.')
    elif response == 'w':
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        if cash_out % 10 != 0:
            print('AMOUNT MUST MATCH 10 EURO NOTES')
        elif cash_out > amounts[n]:
            print('INSUFFICIENT BALANCE')
        else:
            amounts[n] -= cash_out
            print(f'YOUR NEW BALANCE IS: {amounts[n]} RUPEES')
    elif response == 'd':
        cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
        if cash_in % 10 != 0:
            print('AMOUNT MUST MATCH 10 EURO NOTES')
        else:
            amounts[n] += cash_in
            print(f'YOUR NEW BALANCE IS: {amounts[n]} RUPEES')
    elif response == 'p':
        new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
            if new_ppin == new_pin:
                pins[n] = new_pin
                print('NEW PIN SAVED')
            else:
                print('PIN MISMATCH')
        else:
            print('NEW PIN MUST CONSIST OF 4 DIGITS AND BE DIFFERENT FROM PREVIOUS PIN')
    elif response == 'q':
        exit()
    else:
        print('RESPONSE NOT VALID')
