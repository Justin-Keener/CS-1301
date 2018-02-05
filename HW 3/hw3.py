""" 
    Function name (1): rearrange_vowels
    Parameters: string to be iterated through (str)
    Return value: string starting with all of the vowels of the original string, and
    ending with all of the consonants of the original string (str)
    Description: Write a function that takes in a string and separates all of the vowels from the consonants, and creates
    a new string made from the separated portions. The ordering of the vowels and consonants should
    be the same order that they are present in the string. Consider only “a”,”e”,”i”,”o”, and “u” as vowels.
    “Y” should be considered a consonant. Capitalization should also be preserved. Any spaces present
    in the original string should be ignored and not added to the final output. You must use a for loop in
    this function to receive full credit.
"""

def rearrange_vowels(word):
    vowel = ""
    consonant = ""
    for letter in word:
        if letter in "aeiouAEIOU":
            vowel += letter
        else:
            consonant += letter
    return vowel + consonant

print(rearrange_vowels("hello"))
print(rearrange_vowels("Oklahoma"))
print(rearrange_vowels("Computer Science"), "\n")

"""
Function name (2): censor
    Parameters: string to censor (str)
    Return value: censored string (str)
    Description: You are working at a children’s television network, and your job is to censor any words that could
    potentially be inappropriate. In order to do this, you have to replace certain letters with symbols. You
    must use a for loop in this function to receive full credit. The rules for censorship or as follows:
    1. “a” or “A” → “!”
    2. “u” or “U” → “*”
    3. “i” or “I” → “@”
    4. “e” or “E” → “#”
"""
def censor(word):
    next_letter = ""
    for letter in word:
        if letter in "aA":
            next_letter += "!"
        elif letter in "uU":
            next_letter += "*"
        elif letter in "iI":
            next_letter += "@"
        elif letter in "eE":
            next_letter += "#"
        else:
           next_letter += letter
    return next_letter
print(censor("What the heck!"))
print(censor("You smell bad"))
print(censor("I Love CS!"),"\n")

"""
    Function name (3): odd_and_even_multiples
    Parameters: non-zero lower bound of the range and number used to calculate
    multiples (int), upper-bound of a range (int)
    Return value: string displaying the number of odds and evens (str) (follow the
    format below exactly, not having the exact format will result in not receiving
    full credit for this function)
    
    Description: Your function should iterate through a range from the lower bound of the range to the given upper-  
    bound. Count the number of odd and even numbers that are multiples of the first parameter. Ensure

    that the upper bound is actually included in the range for this function. Be sure to return the string in
    the exact format below.
"""

def odd_and_even_multiples(lowerbound,upperbound,):
    counter = 0
    counter1 = 0
    number = lowerbound
    for i in range(lowerbound,upperbound+1):
        if i % lowerbound == 0 and i % 2 == 0:
            counter += 1
        elif i % lowerbound == 1 and i % 2 == 0:
            counter1 += 1
    return print(counter, "even multiple(s) and ", counter1, "odd multiple(s) from",lowerbound,"-",upperbound)

odd_and_even_multiples(2,10)
odd_and_even_multiples(3,14)
odd_and_even_multiples(1,10)
odd_and_even_multiples(-4,8)

"""
    Function name (4): most_common_character
    Parameters: a word or sentence (str), a string containing characters that will be
    counted (str)
    Return value: a string representing which character of the second parameter appears
    most frequently in the phrase string (str).
    Description: Write a function that receives two strings as parameters. The first parameter is a sentence, while the
    second string will contain any combination of characters (letters, numbers, space, special characters,
    etc.). Your code should find which of the given characters in the second parameter appears most
    frequently in the sentence string. Case should not be ignored, so for example, “A” and “a” should be
    considered two different characters. If no characters appear, an empty string should be returned.
"""

def most_common_character(sentence,random_letters):
    max_letter = ""
    char_max = 0
    for i in random_letters: # goes through each letter of random letters
        count = 0
        for letters in sentence: # goes through each letter in the sentence
            if i == letters:
                count += 1
            if char_max < count:
                char_max = count
                max_letter = i
                            
    return max_letter

print(most_common_character("This is a sentence","!aTsn"))
print(most_common_character("Mississippi", "lmnop"))
print(most_common_character("Taylor Swift is bad","mxz"))
print(most_common_character("aaa bbb ccc dddddd","cba"),"\n")

"""
    Function name (5): sum_multiples
    Parameters: non-zero lower bound of the range and number used to calculate
    multiples (int), upper-bound of a range (int)
    Return value: sum of the multiples found in the given range (int)
    
    Description:

    Your function should iterate through a range from the lower bound of the range to the given upper-
    bound, and, using the first parameter (which is also used for the lower bound), calculate the sum of

    any multiples found in the range. Ensure that the upper bound is actually included in the range for
    this function.
"""

def sum_multiples(lowerbound,upperbound):
    count = 0
    for i in range(lowerbound,upperbound+1): # starts from lowerbound then increments to upperbound
        if i % lowerbound == 0:
            count += i
    return count

print(sum_multiples(2,6)) 
print(sum_multiples(1,6))
print(sum_multiples(5,18))
print(sum_multiples(-3,6),"\n")

"""
    Function name (6): remove_vowels
    Parameters: a word (str)
    Return value: original word without vowels (str)
    Description: Write a function that takes a string as a parameter, removes the vowels from the string (upper and
    lowercase). It should return one string, consisting of the same letters of the original string, but without
    the vowels. Consider only “a”,”e”,”i”,”o”, and “u” as vowels. “Y” should be considered a consonant.
    Must iterate through the string.
"""

def remove_vowels(word):
    vowels = "aeiouAEIOU"
    new_letter = ""
    for letter in word:
        if  letter not in vowels:
            new_letter+= letter
    return new_letter

print(remove_vowels("applE"))
print(remove_vowels("mississippi"))
print(remove_vowels("logArithm"),"\n")

"""
    Function name (7): guess_dumplings
    Parameters: number of dumplings ate (int)
    Return value: number of guesses the user took (int)
    Description: Write a function that takes an integer value of the number of dumplings you ate, and asks the user to
    try to guess this number. When the user guesses the correct value, print a congratulatory statement
    and tell them how many guesses it took. If the user inputs “quit” (exactly the string quit, don’t worry
    about edge cases like ‘QUIT’ or ‘Quit’), your code should end, and print the correct answer. The
    integer returned if the user quits should be -1. If the user has not guessed the correct answer within
    the 5th try, print that they’ve lost the game, and return 0. You must use a while-loop.
"""
def guess_dumplings(number_of_dumplings):
    guesses = 0
    msg = ""
    while guesses < number_of_dumplings:
        guess = input(msg + "\nWhat is your guess? ")
        guesses += 1
        if guess == "quit" or guess == "Quit":
            print("The correct answer was " + str(number_of_dumplings))
            return -1        
        elif int(guess) != number_of_dumplings:
            print("Wrong answer, try again\n")
        elif int(guess) == number_of_dumplings: 
            print("Correct! It took you " + str(guesses) + " tries.\n")
            return 0
    print("You lose. The correct answer was " + str(number_of_dumplings))

guess_dumplings(5)

"""
    Function name (8): tie
    Parameters: a number 2-9 specifying half the max width of the tie (int)
    Return value: N/A
    Description: Write a function that takes in a number specifying half the width of the tie as a parameter and prints
    a tie of those specifications. Make sure the tie prints in the correct format as shown in the example
    below. Do not hardcode this. You must use a for-loop (or several).
"""

def tie(half_width):
    count = 0
    for n in range(half_width, 0, -1):
        """
            double = str(n)*(n*2)
                double is assigned to the string n that is printed double of whatever the integer is onto one line
                such as if n = 2, then double = 2222
            print(" "*count)
                This prints the number of spaces that is equal to the number assigned to count
                As count increments by 1, the total number of spaces is incremented too
            print(""*count + double)
                This prints the number of spaces assigned to count, then at the end of the spaces
                is the string of the integer that is being printed twice as much of its integer 
        """        
        double = str(n)*(n *  2)
        print(" "*count + double)
        count += 1
    """
        count is at the value of halfwidth. So the next output 11 will be indented
        compared to the other output 11 one line above. This is why 
        count = half_width - 1 is needed to make sure those two different lines have
        the same indention.
    """
    count = half_width - 1 
    for n in range(1,half_width+1):
        double = str(n)*(n*2)
        print(" "*count + double)
        count -= 1

    count = 0
    for n in range(half_width,0,-1):
        double = str(n)*(n*2)
        print(" "*count + double)
        count += 1
    
tie(5)