import random

keep_playing = True

def shuffle_deck():
    suite_of_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
    full_deck = suite_of_cards * 4
    random.shuffle(full_deck)
    return full_deck
def input_bool(message):
    while True:
        is_yes = input(message + " y/n ").lower()

        if is_yes in ("yes", "y"):
            return True
        elif is_yes in ("no", "n"):
            return False
        else:
            print("Invalid Entry")
def cards_sum(cards):
    total = 0
    aces = 0

    for card in cards:
        if card in ("K", "Q", "J"):
            total += 10
        elif card == "A":
            aces += 1
        else:
            total += int(card)

    # Cal if A's are a 1 or 10
    for ace in range(aces):
        if total > 21:
            total += 1
        else:
            total += 10

    # Cal if Black Jack
    if len(cards) == 2 and total == 21:
        return 0
    else:
        return total
def show_full_hand(cards):
    return " ".join(card for card in cards)
def show_hidden_hand(cards):
    return "[]" * (len(cards) - 1)
def print_endgame_hand(user_cards, computer_cards):
    print(f"Your hand:", show_full_hand(user_cards),
          ">", cards_sum(user_cards))
    print(f"Computer's hand:", show_full_hand(computer_cards),
          ">", cards_sum(computer_cards))

while keep_playing:
    deck = shuffle_deck()
    user_hand = [deck.pop(), deck.pop() ]
    computer_hand = [deck.pop(), deck.pop()]
    user_hit = None
    computer_hit = None

    while True:
        user_score = cards_sum(user_hand)
        computer_score = cards_sum(computer_hand)

        print()

        # Show user the hands they would see when playing
        print("Your Hand:", show_full_hand(user_hand),
              " > ", user_score)
        print("Computer Hand:", computer_hand[0],
              show_hidden_hand(computer_hand))
        print()

        # End the game if there is a winner/loser/draw
        if user_score == 0:
            print("You Win, BlackJack!!!!")
        elif computer_score == 0:
            print("You Lose, BlackJack!!!!")
        elif user_score > 21:
            print("You Lose, you went over")
            print_endgame_hand(user_hand, computer_hand)
            break
        elif computer_score > 21:
            print("You Win, computer went over.")
            print_endgame_hand(user_hand, computer_hand)
            break
        elif user_hit == False and computer_hit == False:
            if user_score > computer_score:
                print("\nYou Win.")
                print_endgame_hand(user_hand, computer_hand)
            elif user_score < computer_score:
                print("\nYou Lose.")
                print_endgame_hand(user_hand, computer_hand)
            else:
                print("\nDraw")
                print_endgame_hand(user_hand, computer_hand)
            break

        # Player's choice if they want to take a card
        user_hit = input_bool("Take a hit?")
        if user_hit:
            user_hand.append(deck.pop())
        if computer_score <= 17:
            computer_hit = True
            computer_hand.append(deck.pop())
        else:
            computer_hit = False

    # Play again? (Ask the user.)
    print()
    keep_playing = input_bool("Play again?")
