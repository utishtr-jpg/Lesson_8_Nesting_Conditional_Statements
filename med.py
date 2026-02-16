med=(input("Please enter if you have a medical condition (Y/N)")).strip().upper()

if med == "Y":
    print("You are allowed")
else:
    attendance=int(input("Enter the number of students"))
    if attendance >= 88:
        print("Your attendance is greater or equal to 88 which means you are allowed")
    else:
        print("Your attendance is lesser than 88 which means you are not allowed")

    