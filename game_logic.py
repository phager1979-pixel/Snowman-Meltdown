from ascii_art import STAGES
from ascii_art import VICTORY

import random
import time

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def create_guessed_word(secret_word):
    guessed_word = list("_" * len(secret_word))
    return guessed_word

def update_guessed_word(guess, secret_word, guessed_word, wrong_guess):
    if guess in secret_word:
        for index, char in enumerate(secret_word):
            if guess == char:
                guessed_word[index] = char
    else:
        wrong_guess += 1
    return guessed_word, wrong_guess

def is_word_guessed(guessed_word, secret_word):
    return "".join(guessed_word) == secret_word

def update_game_screen(wrong_guess, guessed_word):
    print(STAGES[wrong_guess])
    print("Word: " + " ".join(guessed_word))

def firework():

    victory_stage = 0
    while victory_stage < len(VICTORY):
        print(VICTORY[victory_stage])
        victory_stage +=1
        time.sleep(0.25)

def new_game():
    next_round = input("Do you want to play again? Y / N   :")
    if next_round.lower() == "y":
        play_game()
    else:
        print("Thanks for playing - see you later !")


def play_game():
    secret_word = get_random_word()
    wrong_guess = 0
    guessed_letters = set()

    print("Welcome to Snowman Meltdown!")

    # TODO: Build your game loop here.

    guessed_word = create_guessed_word(secret_word)

    while wrong_guess < len(STAGES) - 1:
        update_game_screen(wrong_guess, guessed_word)

        guess = input("Guess a letter: ").lower()


        if guess.isalpha() == False or len(guess) > 1:
            print("Please only enter valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        guessed_word, wrong_guess = update_guessed_word(guess, secret_word, guessed_word, wrong_guess)

        if is_word_guessed(guessed_word, secret_word):
            firework()
            print("Congratulations, you saved the snowman!")
            break

    else:
        update_game_screen(wrong_guess, guessed_word)
        print(f"You lost! The word was: {secret_word}")

    new_game()
