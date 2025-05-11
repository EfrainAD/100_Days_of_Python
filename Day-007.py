def splash_screen():
    print('''
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/
''')
def hangman_img (progress):
    if progress == 6:
        return '''
          +---+
          |   |
              |
              |
              |
              |
        =========
        '''
    elif progress == 5:
        return '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        '''
    elif progress == 4:
        return '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        '''
    elif progress == 3:
        return '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        '''
    elif progress == 2:
        return '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
        '''
    elif progress == 1:
        return '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========
        '''
    else: return ""

splash_screen()

life_counter = 6
word_to_guess = ["h", "e", "l", "l", "o"]
word_guess = ["_", "_", "_", "_", "_"]
letter_left = len(word_to_guess)
guess_list = []

while life_counter > 0 and letter_left > 0 :
    print("Word to guess:", "".join(word_guess))
    guess = input("Guess a letter: ")

    if guess in guess_list:
        print(f"You've already guessed {guess}")
    else:
        guess_list.append(guess)

        if guess in word_to_guess:
            indexs = [i for i, x in enumerate(word_to_guess) if x == guess]
            for i in indexs:
                word_guess[i] = guess
                letter_left -= 1
            print("".join(word_guess))
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            life_counter -= 1

    word_str = "".join(word_to_guess)
    if letter_left <= 0:
        print("YOU WIN")
    elif life_counter > 0:
        print()
        print(hangman_img(life_counter))
        print(f"****************************{life_counter}/6 "
              f"LIVES LEFT****************************")
    else:
        print(f"***********************IT WAS {word_str}! "
              f"YOU LOSE**********************")