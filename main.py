MAX_TRIES = 6
HANGMAN_PHOTOS = {
    0: "    x-------x",
    1:
"""
    x-------x
    |
    |
    |
    |
    |
""",
    2:
"""
    x-------x
    |       |
    |       0
    |
    |
    |
""",
    3:
"""
    x-------x
    |       |
    |       0
    |       |
    |
    |
""",
    4:
"""
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |

""",
    5:
"""
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""",
    6:
"""
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
""",
}

def print_welcome():
    HANGMAN_ASCII = """Welcome to the game Hangman
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_  \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
"""
    print(HANGMAN_ASCII)

def check_win(secret_word, old_letters_guessed):
    for ch in secret_word:
        if ch not in old_letters_guessed:
            return False
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    st = ["_"] * len(secret_word)
    for i, c in enumerate(secret_word):
        if c in old_letters_guessed:
            st[i] = c
    return " ".join(st)

def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed:
        return True
    return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True

    print("X")
    print(' -> '.join(sorted(old_letters_guessed)))
    return False

def choose_word(file_path, index):
    with open(file_path, 'r') as file:
        words = file.read().split()
        return words[index % len(words)]


def main():
    print_welcome()
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    print()
    print("Let’s start!")
    secret_word = choose_word(file_path, index).lower()
    old_letters_guessed = []
    num_of_tries = 0

    print(HANGMAN_PHOTOS[num_of_tries])
    print(show_hidden_word(secret_word, old_letters_guessed))
    print()

    while (num_of_tries < MAX_TRIES) and (not check_win(secret_word, old_letters_guessed)):
        guess = input("Guess a letter: ").lower()
        if try_update_letter_guessed(guess, old_letters_guessed):
            if guess not in secret_word:
                num_of_tries += 1
                print(":(")
                print(HANGMAN_PHOTOS[num_of_tries])
            print(show_hidden_word(secret_word, old_letters_guessed))

    if num_of_tries == MAX_TRIES:
        print(f"LOSE. The word was: {secret_word}")
    else:
        print("WIN")

if __name__ == "__main__":
    main()