# 1** What is 7 to the power of 4?**
x = 7 ** 4
print(f"x = {x}")

#2 ** Split this string:**

s = "Hi there Sam!"
    
# into a list. **
z = s.split()
print(z)

#3 ** Given the variables:**

planet = "Earth"
diameter = 12742

#4 ** Use .format() to print the following string: **
'''
The diameter of Earth is 12742 kilometers.
'''
print(f"The diameter of {planet} is {diameter} kilometers")

# 5 ** Given this nested list, use indexing to grab the word "hello" **
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

v = lst[3][1][2]
print(v)

#6 ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

a = d['k1'][3]['tricky'][3]['target'][3]
print(a) 

# 7 ** What is the main difference between a tuple and a list? **
# Tuple is immutable
'''
The main difference is that lists are mutable, meaning their contents 
can be changed after creation, while tuples are immutable, meaning they cannot be changed once created. 
'''

# 8 ** Create a function that grabs the email website domain from a string in the form: **

#     user@domain.com
    
# **So for example, passing "user@domain.com" would return: domain.com**

def domainGet(email):
    q = email.split("@")
    updatedemail = q[1]
    return updatedemail
print(domainGet('user@domain.com'))

# 9 ** Create a basic function that returns True if the word 'dog' is contained in the input string. 
# Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.
#  **

def findDog(word):
    drow = word.casefold()
    if "dog" in drow:
        return True
    else:
        return False
print(findDog('Is there a dog here?'))
    
# 10 ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **
def countDog(word):
    lower_word = word.casefold()
    if "dog" in lower_word:
        counted_word = lower_word.count("dog")
        return counted_word
    else:
        return False
print(countDog('This dog runs faster than the other dog dude!'))

#11 ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**

#     seq = ['soup','dog','salad','cat','great']

# **should be filtered down to:**

#     ['soup','salad']

seq = ['soup','dog','salad','cat','great']
word_s = list(filter(lambda x: x.startswith('s'),seq)) 
print(word_s)

#12 ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

def caught_speeding(speed, is_birthday):
    if speed <= 60 and is_birthday == False:
        return "No Ticket"
    elif 61 <= speed <= 80 and is_birthday == False:
        return "Small Ticket"
    elif speed >= 81 and is_birthday == False:
        return "Big Ticket"
    elif speed <= 65 and is_birthday == True:
        return "No Ticket"
    elif 66 <= speed <= 85 and is_birthday == True:
        return "Small Ticket"
    elif speed >= 86 and is_birthday == True:
        return "Big Ticket"
print(caught_speeding(81,True))
print(caught_speeding(81,False))