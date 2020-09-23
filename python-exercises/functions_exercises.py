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