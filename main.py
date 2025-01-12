import random

words = {
    0: "Skibidi",
    1: "Gassy",
    2: "Beagle",
    3: "Hamburger"
}

Nword = random.randint(0, 3)
word = words[Nword]
user_guess = ""

while user_guess != word:
    user_guess = input(f"Guess the word:\nHint: it's {len(word)} letter's long!\n").lower()
    
   
    correct_letters = [letter for letter in word if letter.lower() in user_guess]
    
    if correct_letters:
        print(f"You got {len(correct_letters)} letter(s) correct!")
    else:


    
        print("No letters correct. Try again!")

print("Congrats! You've guessed the word.")
# return 0
