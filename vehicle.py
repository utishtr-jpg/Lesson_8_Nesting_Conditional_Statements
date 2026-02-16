print("This program will let you decide what type of vehicle you want")
print("1.Bike")
print("2.Car")

choice=int(input("Enter your choice"))

if choice == 1:
    print("What type of bike do you choose?")
    print("1.Scooter")
    print("2.Motorcycle")
    choice2= int(input("Enter which type of bike"))
    if choice2==1:
        print("You have selected the scooter")
    else: 
        print("You have selected the motorcycle")

elif choice == 2:
    print("What type of car do you choose?")
    print("1.Sedan")
    print("2.SUV")
    choice3= int(input("Enter which type of car"))
    if choice3==1:
        print("You have selected the Sedan")
    else: 
        print("You have selected the SUV")
else:
    print("You have entered an invalid choice")