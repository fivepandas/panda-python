sandwich_orders = ["bacon","cheese","hot dog"]
finished_sandwichies = []

while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print(f"I made your {made_sandwich}.")
    finished_sandwichies.append(made_sandwich)
for finished_sandwichy in finished_sandwichies:
    print(f"{finished_sandwichy}")

