print("Welcome: You should tip!")
total = float(input("Bill amount? $"))
tip = float(input("Tip %? "))
split = float(input("How many people will split the bill? "))

# First Attempt before seeing anything
# print("Each person should pay", (total + total * tip/100)/split)

# Next Attempt before seeing salutation
print(f"Each person should pay {round((total + total * tip/100)/split, 2):.2f}")
2