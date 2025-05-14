# Operations
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def malti(a, b):
    return a * b
def div(a, b):
    return a / b
def mod(a, b):
    return a % b

do_math = {
    "+": add,
    "-": sub,
    "*": malti,
    "/": div,
    "%": mod,
}

def input_float(message):
    while True:
        try:
            return float(input(message))
            # return first
        except:
            print("Not Valid, Try Again.")
def get_operation():
    while True:
        print(" ".join(str(op) for op in do_math))
        operation = input("Pick an operation: ")
        if operation in do_math:
            return operation

print("Calculator App\n")

first = None

while True:
    first = first or input_float("First number: ")
    operation = get_operation()
    second = input_float("second number: ")

    answer = do_math[operation](first, second)

    print(f"{first} {operation} {second} = {answer}")

    while True:
        user_input = input(f"Press c to continue with {answer}\n"
                           f"Press r for restart over\n"
                           f"Press e for exit\n")
        if user_input in ("e", "r", "c"):
            break
        else:
            print("Not Valid, Try Again.")

    if user_input == "e":
        break # Finish App
    elif user_input == "r":
        first = None
        print("New Problem")
    elif user_input == "c":
        first = answer
        print(f"Starting over with {answer}")
