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

#Loop basics

#Create an integer variable i with a value of 5.
i = 5
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.
while i<=15:
    print(i)
    i+=1

#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
x=0
while x<=100:
    print (i,"\n")
    i+=2

#Alter your loop to count backwards by 5's from 100 to -10.
y=100
while y>=-10:
    print (y,"\n")
    i-=5

#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
z=2
while z<=1000000:
    print(z*z)
    z +=1

#Write a loop that uses print to create the output shown below.
a=100
while a>0:
    print(a)
    a-=5
