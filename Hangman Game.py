import random

# Predefined list of words
word_list = ["apple", "chair", "robot", "house", "plant"]

# Choose a random word
chosen_word = random.choice(word_list)

# Create placeholders for guessed letters
guessed_word = ["_"] * len(chosen_word)

# Track guessed letters and number of wrong attempts
guessed_letters = []
wrong_attempts = 0
max_attempts = 6

print(" Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 chances to guess wrong.\n")

while wrong_attempts < max_attempts and "_" in guessed_word:
    print("Word: ", " ".join(guessed_word))
    print("Guessed letters: ", ", ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                guessed_word[i] = guess
        print(" Correct guess!\n")
    else:
        wrong_attempts += 1
        print(f" Wrong guess! You have {max_attempts - wrong_attempts} chances left.\n")

# Game result
if "_" not in guessed_word:
    print(" Congratulations! You guessed the word:", chosen_word)
else:
    print(" Game Over! The word was:", chosen_word)
