import random
import string

new_password = []

print("Welcome to the PyPassword Generator!")
num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like?\n"))
num_of_numbers = int(input("How many numbers would you like?\n"))


for i in range(num_of_letters):
    new_password.append(random.choice(string.ascii_letters))
for i in range(num_of_numbers):
    # index = int(random.random() * len(new_password))
    # new_number = random.choice(string.digits)

    # new_password.insert(index, new_number)
    # new_password.append(new_number))
    new_password.append(random.choice(string.digits))

for i in range(num_of_symbols):
    # index = int(random.random() * len(new_password))
    # new_symbols = random.choice(string.punctuation)

    # new_password.insert(index, new_symbols)
    # new_password.append(new_symbols)
    new_password.append(random.choice(string.punctuation))

random.shuffle(new_password)
print("\nYour password is:", "".join(new_password))
