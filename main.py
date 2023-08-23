import os
import random
import sys


def print_game_header():
    print('Welcome to Guess the Word!')
    print('This is a game that generates a word and you have to guess it.\n')


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    play_again = True

    retry_response = True
    response = ""

    while play_again:
        print_game_header()
        print('You have three attempts to guess the word.')
        print('Any matching characters will be highlighted.\n')

        while retry_response:
            print("------------------------------")
            print('Difficulty Levels\n  1 - Easy\n  2 - Medium\n  3 - Hard')
            print("------------------------------\n")

            retry_response = False

            response = input(f"Please select a difficulty level (1-3): ")

            if response not in ['1', '2', '3']:
                os.system('cls')
                print('Invalid difficulty was selected. Please try again using (1-3).')
                retry_response = True

        retry_response = True

        words = open(resource_path("data/words.txt")).read().splitlines()

        match response:
            case "1":
                words = filter(lambda word: len(word) <= 3, words)
            case "2":
                words = filter(lambda word: 7 > len(word) > 3, words)
            case "3":
                words = filter(lambda word: len(word) >= 7, words)

        words = list(words)

        index = random.randint(0, len(words) - 1)
        selected_word = words[index]

        word_length = len(selected_word)
        display_word = "_" * word_length

        os.system('cls')

        for i in range(3):

            print("----------------------------------------------")

            while retry_response:
                print(f'Your word consists of {word_length} letters.')
                print(f'\n{display_word}\n')
                print("----------------------------------------------")
                retry_response = False

                response = input(f"Please enter a guess: ")

                response_length = len(response)

                if response_length != word_length:
                    os.system('cls')
                    if response_length > word_length:
                        print(f'Too many letters entered! Please try again.')
                    elif response_length < word_length:
                        print(f'Not enough letters entered! Please try again.')

                    retry_response = True

            retry_response = True

            for letter in response:
                letter_count = selected_word.count(letter)

                search_array = list(selected_word)

                for _ in range(letter_count):
                    index = search_array.index(letter)

                    search_array[index] = ""

                    if index != -1:
                        display_list = list(display_word)
                        display_list[index] = letter
                        display_word = "".join(display_list)

                os.system('cls')

            if display_word == selected_word and selected_word == response:
                print(f"Won! Congrats!")
                break
            elif i == 2 or (display_word == selected_word and selected_word != response):
                if display_word == selected_word and selected_word != response:
                    print("All matching letters were found, but the guess did not match.\n")

                print(f"You Lost! Please try again.")
                break

        print(f"The correct word was \"{selected_word}\".\n")

        while retry_response:
            retry_response = False

            response = input(f"Would you like to play again? (Y/N): ")
            response = response.lower()

            if response == 'n':
                play_again = False
            elif response == 'y':
                os.system('cls')
            else:
                retry_response = True
                os.system('cls')
                print(f'Invalid response. Please respond with "Y" or "N".')

        retry_response = True
