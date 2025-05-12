letters = "abcdefghijklmnopqrstuvwxyz"
run = True

while run:
    # Get user's inputs
    while True:
        user_input = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
        mode = "encrypt" if user_input == 'e' else "decrypt" if user_input == 'd' else None
        if mode is not None:
            break
        print("Not a valid entry.\n")

    message = input(f"Type your message you want to {mode}ed:\n")
    while True:
        user_input = input(f"Type in the {mode}ion key:\n")
        try:
            encryption_key = int(user_input) % 26
            print("encryption_key", encryption_key)
            break
        except ValueError:
            print(f"\"{user_input}\" is not a valid entry.\n")

    # Encrypt or Decrypt
    new_message = ''
    for i, letter in enumerate(message):
        if not letter.isalpha():
            new_message += letter
        else:
            letter_index = letters.find(letter.lower())
            # You can change encryption key to a negative number if it's decrypting,
            # however I left it this way because it's more readable.
            if mode == "encrypt":
                cryption_index = (letter_index + encryption_key) % 26
            else:
                cryption_index = (letter_index - encryption_key) % 26
            new_message +=  letters[cryption_index] if letter.islower() else letters[cryption_index].upper()

    # Finished: display the outcome
    print(f"\n{mode.capitalize()}ed message:", new_message, "\n")

    # End App?
    user_input = input("Finished? y = yes, anything else = no\n")
    print('')
    run = False if user_input.lower() == 'y' else True
