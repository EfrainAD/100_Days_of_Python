import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty in ("easy", "hard"):
        break

life_count = 5 if difficulty == "hard" \
    else 10 if difficulty == "easy" \
    else None
answer = random.randint(1, 100)

for i in range(life_count):
    message = " now " if i > 0 else " "
    print(f"You{message}have {life_count} attempts to guess the number.")

    guesses = int(input("Make a guess: "))

    if guesses > answer:
        print("Too High! Lose a life!")
        life_count -= 1
    elif guesses < answer:
        print("Too Low! Lose a life!")
        life_count -= 1
    else:
        print("You Got it! It was", answer, "! The End.")
        break
    if life_count <= 0:
        print("You've out of lives...... The End.")
        break