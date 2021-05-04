# 1. SIGNUP STAGE
# Create Account
# Input: First Name | Last Name | e-Mail | Phone Number
# Generate Account Number for User


# 2. LOGIN STAGE
# Login with Account Number and Password


# BANK ACTIVITY STAGE

# initialize system
import random
import validation
import database
from getpass import getpass


#-- List of all Functions (so I don't mix them.)
#-- def initial()
#-- def login()
#-- def signup()
#-- def bank_activity()
#-- def withdrawal_activity()
#-- def deposit_activity
#-- def create_account_number()
#-- def set_current_balance ()
#-- def get_current_balance()
#-- def logout()


def initial():
    print("Welcome to UmoruBank LoL")

    got_account = int(input("Got an account with us? 1 (yes) 2 (no) \n"))

    if got_account == 1:

        login()

    elif got_account == 2:

        signup()

    else:
        print("Option selected doesn't exist. Please try again.")
        initial()


def login():
    print("----- User Login -----")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password);

        if user:
            bank_activity(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: please check that you have up to 10 digits and only whole numbers, not decimals")
        initial()


def signup():
    print("-------New User Registration -------")

    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("What is your email address? \n")
    password = getpass("Create a password for yourself \n")

    account_number = create_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created!")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Oops! Something went wrong. Please try again")
        signup()


def bank_activity(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_activity()
    elif selected_option == 2:

        withdrawal_activity()
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bank_activity(user)


def withdrawal_activity():
    print("withdrawal")
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance


def deposit_activity():
    print("Deposit Operations")
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance


def create_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    login()


initial()
