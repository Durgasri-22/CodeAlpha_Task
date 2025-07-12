import random

# List of 5 predefined words
word_list = ["apple", "house", "green", "tiger", "plant"]

# Choose a random word from the list
secret_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Create a display version of the word with underscores
display_word = ["_" for _ in secret_word]

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.")
print(" ".join(display_word))

while incorrect_guesses < max_guesses and "_" in display_word:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i, letter in enumerate(secret_word):
            if letter == guess:
                display_word[i] = guess
        print("Correct!")
    else:
        incorrect_guesses += 1
        print(f"Incorrect! You have {max_guesses - incorrect_guesses} guesses left.")

    print(" ".join(display_word))

# Check final result
if "_" not in display_word:
    print("Congratulations! You guessed the word!")
else:
    print(f"Game over! The word was '{secret_word}'.")
