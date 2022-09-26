"""
Guess The Word

9/21/2022

2ish weeks coding
"""
import random

from words import words

# picks random word from list
word = str(random.choice(words))
# makes word lower case
word = word.lower()
# counts number of letters in words
word_length = len(word)

# prints word for testing purpose
# print('||||||||||||||||||||||||||||||')
# print('The Word Is: ', word)
# print('||||||||||||||||||||||||||||||')

# Define hints, [] to grab the letter at a certain position in the word
hint1: str = word[0]
hint2 = word[int(word_length - 1)]
hint3 = word[int(word_length - (word_length / 2))]


def guess_the_word():
    # limit tries to 50
    tries = 50
    # gets user input and makes it lower case
    user_guess = input("Enter Word: ")
    user_guess = user_guess.lower()

    # first try clause
    if user_guess == word:
        print('First Try')
    elif user_guess != word:
        while user_guess != word:
            # Lower tries by 1 and tells you when you get it wrong each time you guess wrong
            if user_guess != word:
                print('Nope Try Again')
                tries = tries - 1
            # asks user if they want a hint at 40, 20 and 5 tries
            if tries == 40:
                print('want a hint? it will cost a guess')
                choice = input('(Yes/No): ')
                choice = choice.lower()
                if choice == 'yes':
                    print('The first letter is ', str(hint1))
                    print('The word is ', str(word_length), ' letters long')
                    tries = tries - 1
                elif choice == 'no':
                    print('Okay')
            if tries == 20:
                print('want a hint? it will cost a guess')
                choice = input('(Yes/No): ')
                choice = choice.lower()
                if choice == 'yes':
                    print('The first letter is ', str(hint2))
                    print('The word is ', str(word_length), ' letters long')
                    tries = tries - 1
                elif choice == 'no':
                    print('Okay')
            if tries == 5:
                print('want a hint? This Ones Free!')
                choice = input('(Yes/No): ')
                choice = choice.lower()
                if choice == 'yes':
                    print('The first letter is ', str(hint3))
                    print('The word is ', str(word_length), ' letters long')
                    tries = tries - 1
                elif choice == 'no':
                    print('Okay')
            print('You Have ', str(tries), ' Tries Remaining')
            # lets you escape the while by guessing the right word
            user_guess = input("Enter Word: ")
            user_guess = user_guess.lower()
            # if user runs out of tries they fail
            if tries == 0:
                print('Sorry you failed')
                break
    # Win clause
    if user_guess == word:
        print('Correct')


# Calls function
play_ = input('Do you want to play guess a word: ')
play_ = play_.lower()
if play_ == 'yes':
    print('The word is ', str(word_length), ' letters long')
    print('You Have 50 Tries Remaining')
    guess_the_word()
elif play_ == 'no':
    print('Well Fuck You Then')
