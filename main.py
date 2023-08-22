import random


def print_game_header():
    print('Welcome to Guess the Word!\n')
    print('This is a game that generates a word and you have to guess it.')
    print('You have three attempts to guess the word.')
    print('Any matching characters will be highlighted and will fill the blanks.')


def generate_word_description(word):
    length = len(word)
    print(f'\nYour word consists of {length} letters')


if __name__ == '__main__':
    words = open("data/words.txt").read().splitlines()

    print_game_header()
    index = random.randint(0, len(words) - 1)

    selected_word = words[index]

    display_word = "_"*len(selected_word)
    generate_word_description(selected_word)

    for i in range(3):

        print(f'\n{display_word}\n')

        response = input(f"\nPlease enter a guess: ")

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

        if display_word == selected_word:
            print(f"\nYou Won! Congrats!")
            break
        elif i == 3:
            print(f"\nYou Lost! Please try again")

    print(f"The correct word was {selected_word}")
