from draw import *
# from wordlist import wordlist


import random

MAX_TRIES = 6

print(HANGMAN_ASCII_ART)
# answer = input('admin: enter your answer here:> ')
answer = 'a'

def guess():
    attempts = 0
    while True:
        guess = input('enter your guess here: [X] to stop ')
        if guess == answer :
            print('congratulations, you won!')
            break
        if guess == 'X':
            print('you\'ve chosen to exit, too bad... !')
            break
        else:
            attempts = attempts +1
            if attempts == 0:
                print(attempt1)
            elif attempts == 1:
                print(attempt2)
            elif attempts == 2:
                print(attempt3)
            elif attempts == 3:
                print(attempt4)
            elif attempts == 4:
                print(attempt5)
            elif attempts == 5:
                print(attempt6)
            elif attempts == 7:
                print(attempt7, 'Game over... you died...')
                exit(0)


            # attempt = 'attempt{0)'.format(attempts)

            print('wrong answer, try again... number of tries: ', attempts)
            continue

if __name__ == '__main__':
   guess()