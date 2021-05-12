def make_sandwiches(*toppings):
    print(f"\nyour sandwiches include toppings as follows: ")
    for topping in toppings:
        print(topping)
make_sandwiches('mushroom')
make_sandwiches('mushroom','cheese')
make_sandwiches('mushroom','cheese','lobster')