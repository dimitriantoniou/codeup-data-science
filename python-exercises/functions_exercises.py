# 1Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(n):
    if n ==2:
        print (True)
        return True
    else:
        print (False)    
        return False
        
is_two(2)
is_two(3)

#2 Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(str):
    if str == 'a' or str == 'e' or str == 'i' or str == 'o' or str == 'u':
        print(True)
        return True
    else:
        print(False)
        return False
is_vowel('a')
is_vowel('f')

#3 Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(str):
    if str != 'a' and str != 'e' and str != 'i' and str != 'o' and str !='u':
        print(True)
        return True
    else:
        print(False)
        return False

is_consonant('f')
is_consonant('e')


#4 Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_consonant(str):
    if is_consonant(str[0]):
        print (str.capitalize())
        return str.capitalize()
    else:
        print (str)
        return str

capitalize_consonant('hello')
capitalize_consonant('aww')

#5 Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
#6 Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
#7 Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
#Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
#Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores
#for example:
#Name will become name
#First Name will become first_name
#% Completed will become completed
#Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
