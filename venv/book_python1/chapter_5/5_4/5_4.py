requsted_toppings = ['mushrooms','green peppers','extra cheese']
for requsted_topping in requsted_toppings:
    if requsted_topping == 'green peppers':
        print("sorry,we are out of green peppers right now.")
    else:
        print(f"Adding {requsted_topping}.")
print("\nFinished making your pizza!")