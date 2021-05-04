name = input("Please enter your name \n")
allowedUsers = ["Seyi","Ope","Derin"]
allowedPassword = ["passSeyi", "passOpe", "passs Derin"]

if(name in allowedUsers):
    password = input("Please enter your password \n")
    userID = allowedUsers.index(name)

    if(password == allowedPassword[userID]):
        
        print("Welcome! Hop right in, %s" % name)
        
        import datetime
        now = datetime.datetime.now()
        print("Current date and time is:")
        print(now.strftime("%y-%m-%d %H:%M:%S"))

        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Make a Complaint")

        selectedOption = int(input("Please select an option:"))
        if(selectedOption == 1):
            input("How much would you like to withdraw?")
            print("Take your cash.")

        elif(selectedOption == 2):
            currentBalance = input("How much would you like to deposit?")
            print("Current Balance: %s" % currentBalance )

        elif(selectedOption == 3):
            input("What issue will you like to report?")
            print("Thank you for contacting us.")

        
            
    else:
        print("Password Incorrect. Please try again.")

else:
    print("Name incorrect. Please try again.")

