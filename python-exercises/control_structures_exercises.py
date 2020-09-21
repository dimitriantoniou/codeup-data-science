#Conditional Basics

#prompt the user for a day of the week, print out whether the day is Monday or not
answer=input("Enter a day of the week: ")
if answer == "Monday":
    print (True)
else:
    print (False)

#prompt the user for a day of the week, print out whether the day is a weekday or a weekend
answer_2=input("Enter a day of the week: ")
if answer_2 == "Saturday" or answer == "Sunday":
    print("Weekend")
else:
    print("Weekday")

#create variables and make up values for
    #the number of hours worked in one week
    hours = 40
    #the hourly rate
    wage = 20
    #how much the week's paycheck will be
    paycheck = hours*wage
    #write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
    paycheck = hours*wage+(hours-40)*wage*.5