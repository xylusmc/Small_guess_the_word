"""
Guess The Word

9/21/2022
9/22/2022
2ish weeks coding in total

calling it, its good enough :)
"""
import random

from words import words

# picks random word from list and makes word lower case
word = str(random.choice(words)).lower()
# counts number of letters in words
word_length = len(word)

# prints word for testing purpose
print('||||||||||||||||||||||||||||||')
print('The Word Is: ', word)
print('||||||||||||||||||||||||||||||')

# Define hints, [] to grab the letter at a certain position in the word
hint1 = word[0]
hint2 = word[int(word_length - 1)]
hint3 = word[1]


def guess_the_word():
    # limit tries to 20
    tries = 20
    # gets user input and makes it lower case
    user_guess = input("Enter Word: ").lower()

    # first try clause
    if user_guess == word:
        print('First Try')
    elif user_guess != word:
        while user_guess != word:
            # Lower tries by 1 and tells you when you get it wrong each time you guess wrong
            print('Nope Try Again')
            tries = tries - 1
            print('You Have ', str(tries), ' Tries Remaining')
            user_guess = input("Enter Word: ").lower()
            # asks user if they want a hint at 16, 11 and 6 tries
            if tries == 16:
                print('want a hint? it will cost a guess')
                choice = input('(Yes/No): ').lower()
                while True:
                    if choice == 'yes':
                        print('The first letter is ', str(hint1))
                        print('The word is ', str(word_length), ' letters long')
                        user_guess = input("Enter Word: ").lower()
                        break
                    elif choice == 'no':
                        print('Okay')
                        user_guess = input("Enter Word: ").lower()
                        break
                    elif choice != 'yes' or 'no':
                        print('Enter a valid input')
                        choice = input('Do you want a hint?: ')
            if tries == 11:
                print('want a hint? it will cost a guess')
                choice = input('(Yes/No): ').lower()
                while True:
                    if choice == 'yes':
                        print('The second letter is ', str(hint3))
                        print('The word is ', str(word_length), ' letters long')
                        user_guess = input("Enter Word: ").lower()
                        break
                    elif choice == 'no':
                        print('Okay')
                        user_guess = input("Enter Word: ").lower()
                        break
                    elif choice != 'yes' or 'no':
                        print('Enter a valid input')
                        choice = input('Do you want a hint?: ')
            if tries == 6:
                print('want a hint? This Ones Free!')
                choice = input('(Yes/No): ').lower()
                while True:
                    if choice == 'yes':
                        print('The last letter is ', str(hint2))
                        print('The word is ', str(word_length), ' letters long')
                        user_guess = input("Enter Word: ").lower()
                        break
                    elif choice == 'no':
                        print('Okay')
                        user_guess = input("Enter Word: ").lower()
                        break
                    elif choice != 'yes' or 'no':
                        print('Enter a valid input')
                        choice = input('Do you want a hint?: ')

            # lets you escape the while loop by guessing the right word

            # if user runs out of tries they fail
            if tries == 1:
                print('Sorry you failed')
                print('The word was: ', word)
                break
        # Win clause
        if user_guess == word:
            print('Correct!!!!')


# Calls function


while True:
    play_ = input('Do you want to play guess a word (Yes/No): ').lower()
    if play_ == 'yes':
        print('The word is ', str(word_length), ' letters long')
        print('You Have 20 Tries, Good Luck!')
        guess_the_word()
        break
    elif play_ != 'yes' or 'no':
        print('Enter a valid input')
    elif play_ == 'no':
        print('Phht okay dude')
        break
