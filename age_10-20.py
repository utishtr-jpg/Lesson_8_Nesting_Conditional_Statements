print("Hello! This program will check if the user's entered agecis one of the ages from 10 to 20.")
age=int(input("Please enter your age!"))

if age >= 10:
    if age <= 20:
        print("Your age is between 10 and 20 years.")
    else:
        print("Your age is greater than 20.")
else:
    print("Your age is less than 10, meaning it is not in between 10 and 20.")

print("Thank you for using this program!")
#end