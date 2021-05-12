class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaurant(self):
        print(f'The name of the restaurant is {self.name}.')
        print(f"The type of the restaurant is {self.type}.")
    def open_restaurant(self):
        print('the restaurant is opening.')
r1=Restaurant('haidilao','hot pot')
print(r1.name)
print(r1.type)
r1.describe_restaurant()
r1.open_restaurant()