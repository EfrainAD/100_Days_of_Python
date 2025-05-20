import random
from game_data import data as game_data

def get_person():
    return game_data.pop(random.randrange(len(game_data)))
def display_person_info(person):
    print(f'Person A: {person["name"]}, {person["description"]}, from {person["country"]}')

# START
score = 0
is_game = True
keep = get_person()

print("Hi, welcome to the comparing game. How good can you guess?\n")
while is_game:
    # Get people from the list
    person_1 = keep
    person_2 = get_person()

    # Inform the user of their options
    display_person_info(person_1)
    display_person_info(person_2)

    # Get the user's guess
    while True:
        guess = input("Guess A or B: ").lower()
        print()
        if guess in ("a", "b"):
            break

    # Check the answer and continue
    answer = "a" if person_1["follower_count"] > person_2["follower_count"] else "b"
    if guess == answer:
        score += 1
        keep = person_1 if answer == "a" else person_2
        print("You got it! Current score:", score)
        # If user answers all the questions, and no more to go.
        if len(game_data) == 0:
            print("You have answered all the guesses correctly!\nYou are a MASTER\nGAME OVER!")
            is_game = False
    else:
        print("Sorry, that's wrong. Final score:", score)
        is_game = False
