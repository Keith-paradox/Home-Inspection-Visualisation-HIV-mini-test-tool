# Name: Min Khant Thu
# Program Name: Home Inspection Visualisation mini test tool program
# Date: 8 November 2021
# Purpose: mini program to input and store the data that user gives and output the specific data that user wants

# use datetime to check if the user input the date and time input correctly
from datetime import datetime
userName = input("Enter your name: ")
print(f"Hi!, {userName}. Welcome to the Home Inspection Visualisation(HIV) mini test tool program.")

startProgram = input("Do you want to start this program?(Enter 'y' for 'yes' and 'n' for 'no'): ").lower().strip()
# this loop will check if you put the correct input or not
while type(startProgram) == str:
    if startProgram == "y":
        print("...\n...\nPROGRAM STARTED")
        break
    elif startProgram == "n":
        quit()
    # if the input is not what we expected this will run
    else:
        print("Input not clear, try again.")
        startProgram = input("Do you want to start this program?(Enter 'y' for 'yes' and 'n' for 'no'): ").lower().strip()

# This is a function to add the reports that user input to .txt file
def putInputs(num, location, hazard, risk, demographicDATE, demographicTIME):
    f = open('input.txt', 'a')
    f.write(f"\n{num}. Location - {location}, Type of anomaly - {hazard}, Level of risk - {risk}, Demographic - {demographicDATE} ({demographicTIME})")

num = 1
# This will renew the last .txt file for completely new reports
refreshFile = open('input.txt', 'w')
while startProgram == 'y':
    # The data entry for each parameters set
    # use .lower to ignore the cases and .strip to ignore spaces in user's input
    location = input("\nOptions for location\n"
                     ">>> Living room, Dining room, Kitchen, Bedroom, Bathroom, Guest room, Basement, Home office\n"
                     "Enter the location of the building: ").lower().strip()
    while type(location) == str:
        if location == "living room":
            break
        elif location == "dining room":
            break
        elif location == "kitchen":
            break
        elif location == "bedroom":
            break
        elif location == "bathroom":
            break
        elif location == "guest room":
            break
        elif location == "basement":
            break
        elif location == "home office":
            break
        # This will run if the user input is not what we expected
        else:
            print("Input cannot be registered, try again.")
            # This will ask the user input until the user gives the correct one
            location = input("Enter the location of the building: ").lower().strip()

    hazard = input("\nOptions for the type of hazard\n"
                   ">>> Water Leakage, Fire Hazard, Electricity Outage, Physical Hazard, Chemical Hazard, Burglary\n"
                   "Enter the type of hazard: ").lower().strip()
    while type(hazard) == str:
        if hazard == "water leakage":
            break
        elif hazard == "fire hazard":
            break
        elif hazard == "electricity outage":
            break
        elif hazard == "physical hazard":
            break
        elif hazard == "chemical hazard":
            break
        elif hazard == "burglary":
            break
        else:
            print("Input cannot be registered, try again.")
            hazard = input("Enter the type of hazard: ").lower().strip()

    risk = input("\nOptions for the level of risk\n"
                 ">>> Seriously High, High, Medium, Low, None\n"
                 "Enter the level of risk: ").lower().strip()
    while type(risk) == str:
        if risk == "high":
            break
        elif risk == "seriously high":
            break
        elif risk == "medium":
            break
        elif risk == "low":
            break
        elif risk == "none":
            break
        else:
            print("Input cannot be registered, try again.")
            risk = input("Enter the level of risk: ").lower().strip()

    demographicDATE = input("\nEnter the date(in DD-MM-YY format) that hazard occurred: ").strip()
    # This is to check if the user input the date in correct format as asked and will ask again if it is not correct
    while type(demographicDATE) == str:
        try:
            datetime.strptime(demographicDATE, "%d-%m-%y")
            break
        except ValueError:
            print("Input cannot be registered, try again.")
            demographicDATE = input("Enter the date(in DD-MM-YY format) that hazard occurred: ").strip()

    demographicTIME = input("\nEnter the time(24-hour time format with : in between) that hazard occurred: ").strip()
    # This will check if the user input the time in correct format or not
    while type(demographicTIME) == str:
        try:
            datetime.strptime(demographicTIME, "%H:%M")
            break
        except ValueError:
            print("Input cannot be registered, try again.")
            demographicTIME = input("Enter the time(24-hour time format with : in between) that hazard occurred: ").strip()
    # After the the inputs are taken it run the putInputs function and add those inputs to .txt file
    putInputs(num, location, hazard, risk, demographicDATE, demographicTIME)
    num += 1
    # check if user wants to input more reports
    startProgram = input("Do you want to add another report?(Enter 'y' for 'yes' and 'n' for 'no'): ").lower().strip()
    while type(startProgram) == str:
        if startProgram == "y":
            print("\nFor a new report")
            break
        elif startProgram == "n":
            break
        else:
            print("Input not clear, try again.")
            startProgram = input("Do you want to add another report?(Enter 'y' for 'yes' and 'n' for 'no'): ").lower().strip()

# selection for report
def search():
    count = 0
    locationSelection = input("\nOptions to search for location\n"
                              ">>> Living room, Dining room, Kitchen, Bedroom, Bathroom, Guest room, Basement, Home office\n"
                              "Enter the location you want to see report of: ").lower().strip()
    while type(locationSelection) == str:
        if locationSelection == "living room":
            break
        elif locationSelection == "dining room":
            break
        elif locationSelection == "kitchen":
            break
        elif locationSelection == "bedroom":
            break
        elif locationSelection == "bathroom":
            break
        elif locationSelection == "guest room":
            break
        elif locationSelection == "basement":
            break
        elif locationSelection == "home office":
            break
        else:
            print("Input doesn't exist, try again.")
            locationSelection = input("Enter the location you want to see report of: ").lower().strip()

    hazardSelection = input("\nOptions to search for the type of hazard\n"
                            ">>> Water Leakage, Fire Hazard, Electricity Outage, Physical Hazard, Chemical Hazard, Burglary\n"
                            "Enter the type of hazard you want to see the report of: ").lower().strip()
    while type(hazardSelection) == str:
        if hazardSelection == "water leakage":
            break
        elif hazardSelection == "fire hazard":
            break
        elif hazardSelection == "electricity outage":
            break
        elif hazardSelection == "physical hazard":
            break
        elif hazard == "chemical hazard":
            break
        elif hazard == "burglary":
            break
        else:
            print("Input doesn't exist, try again.")
            hazardSelection = input("Enter the type of hazard you want to see the report of: ").lower().strip()
    # this will read the .txt file where inputs are stored
    readFile = open('input.txt', 'r')
    for i in enumerate(readFile):
        # to check how many reports are given
        x = len(i)-1
        # to search for the specific report from all the reports given
        while x >= count:
            count += 1
            for line, position in enumerate(readFile):
                # This will search for the location and hazard asked from every line of report
                searchforlocation = locationSelection in position
                searchforhazard = hazardSelection in position
                if searchforlocation == True and searchforhazard == True:
                    # This will run when both location and hazard are found in the report
                    print(f"\nShowing the report of {locationSelection} {hazardSelection}:\n", position[3:].replace(",","\n"))

        print("The reports you've searched for is either already found or doesn't exist.\n")
        runAgain = input(
            "Do you want to search for another report?(Enter 'y' for 'yes' and 'n' for 'no'): ")
        while type(runAgain) == str:
            if runAgain == 'y':
                search()
            elif runAgain == 'n':
                print("This is the summary of all the data collected: ")
                data = open("input.txt")
                lines = data.readlines()
                for line in lines:
                    print(line.replace("\n","").replace(",","\n"))
                    print("-----------------------------------------")
                print(f"\nThank you, {userName} for using this program.\nPROGRAM ENDED")
                quit()
            else:
                print("Input not clear, try again.")
                runAgain = input(
                    "Do you want to search for another report?(Enter 'y' for 'yes' and 'n' for 'no'): ")
# After taken all the import the search function will run and will search for the report that user selected
search()