#float
type(99.9)

"False"
#str
type("False")

False
#bool
type(False)

'0'
#str
type('0')

0
#int
type(0)

True
#bool
type(True)

'True'
#str
type('True')

[{}]
#tuple
type([{}])

{'a': []}
#dict
type({'a':[]})


print('1' + 2)
#12
print(6 % 4)
#2
type(6 % 4)
#int
type(type(6 % 4))
#int
print('3 + 4 is ' + 3 + 4)
#3 + 4 is 7
print(0 < 0)
#false
print('False' == False)
#true
print(True == 'True')
#true
print(5 >= -5)
#true
#print(!False or False)
#true
print(True or "42")
#true
#print(!True && !False)
#false
print(6 % 5)
#1
print(5 < 4 and 1 == 1)
#false
print('codeup' == 'codeup' and 'codeup' == 'Codeup')
#false
#print(4 >= 0 and 1 !== '1')
#false
print(6 % 3 == 0)
#true
print(5 % 2 != 0)
#true
print([1] + 2)
#undefined
print([1] + [2])
#1,2
[1] * 2
[1] * [2]
[] + [] == []
{} + {}


#You have rented some movies for your kids: 
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and 
# Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

mermaid = 3
bear = 5
hercules = 1
total = 3*(mermaid+bear+hercules)
print total

#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. 
# Google pays 400 dollars per hour, 
# Amazon 380, and 
# Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google_rate=400
google_hours=6
amazon_rate=380
amazon_hours=4
facebook_rate=350
facebook_hours=10

wages=google_rate*google+hours+amazon_rate*amazon_hours+facebook_rate*facebook_hours 

#A student can be enrolled to a class only if the class is not full and 
# the class schedule does not conflict with her current schedule.

if (full=false and conflict=false){
    enrolled=true
}


#A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

if(premium === true){
    offer=true
}else{
    if(items >=2 and expired===false){
        offer=true
    }else{
        offer=false
    }
}

#reate a variable that holds a boolean value for each of the following conditions:

#the password must be at least 5 characters
password_long_enough = true
#the username must be no more than 20 characters
password_short_enough = true
#the password must not be the same as the username
match=false
#bonus neither the username or password can start or end with whitespace

#done