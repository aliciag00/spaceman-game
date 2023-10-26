import random 
from words import words
import string

def load_word(words):
  
    secret_word = random.choice(words)
    return secret_word

    

def spaceman():
   
    secret_word = load_word(words)
    secret_word_letters = list(secret_word)
    alphabet = set(string.ascii_lowercase)

    used_letters = set()
    wrong_guess = 7

    secret_word_list = ['_' if letter in secret_word_letters else ' ' for letter in string.ascii_lowercase]

    while len(secret_word_letters) > 0 and wrong_guess > 0:
        print('You have used these letters: ', ' '.join(used_letters))

        secret_word_list = [letter if letter in used_letters else ' ' for letter in secret_word_letters]
        print('Current word:', ' '.join(secret_word_list))

        guessed_letters = input("Guess one letter: ")
    
        if guessed_letters in alphabet - used_letters:
            used_letters.add(guessed_letters)
            if guessed_letters in secret_word_letters:
                secret_word_letters.remove(guessed_letters)
                for i, letter in enumerate(secret_word):
                    if letter == guessed_letters:
                        secret_word[i] = guessed_letters
            else:
                wrong_guess = wrong_guess - 1 
                print(f'\nLetter is not in word. {wrong_guess} guesses remaining.')

        elif guessed_letters in used_letters:
            print(f"\nYou have already guessed {guessed_letters}. Choose another letter: ")

        else:
            print("\nError. That is an invalid letter.")

    if wrong_guess == 0:
        print(f'Sorry! You lose. the secret word was {secret_word}')

    else:
        print(f'You got it! The secret word was {secret_word}')

if __name__ == '__main__':
    spaceman()

    

