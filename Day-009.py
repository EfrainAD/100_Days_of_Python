import os

bids = []
winner = {"name": None, "bid": float('-inf')}

while True:
    name = input("What is your name?: ")
    while True:
        try:
            bid = float(input("What is your bid?: $"))
            if bid <= 0:
                print("Not a valid entry.")
                continue
            break
        except ValueError:
            print("Not a valid entry.")
    while True:
        is_more = input("Are there any other bidders? Type 'yes' or 'no'. ")
        if is_more.lower() in ('yes', 'no'):
            break

    bids.append({"name": name, "bid": bid})
    print("/n" * 100)

    if is_more.lower() == "no":
        break

for bid in bids:
    if bid["bid"] > winner["bid"]:
        winner = bid

print(f"\nThe winner is {winner['name']} with a bid of ${winner['bid']:.2f}")