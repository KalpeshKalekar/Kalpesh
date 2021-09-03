import random   
from word_list import word_list
import string
from hangman_visual import live_visual_dict


def get_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()

def hangman():
    word = get_word(word_list)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # letters user has guessed

    lives = 7
    # getting user input 

    while len(word_letters) > 0 and lives > 0 :

        print('You have', lives, 'lives left You have guessed these letters', ' '.join(used_letters))

        word_lists = [ letter if letter in used_letters else '-' for letter in word]
        print(live_visual_dict[lives])
        print('Current word is ', ' '.join(word_lists))


        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives -1 # takes away a life
                print('\nLetter is not in the word.')

        elif user_letter in used_letters:
            print('\nYou already guessed that letter, Please try another letter')

        else:
            print('\nInvaild Character, Please try again')

    if lives == 0:
        print(live_visual_dict[lives])
        print('Sorry You Died, The word Was', word)

    else:
        print('You guessed the word correctly', word, '!!')


if __name__ == '__main__':
    hangman()



