class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f'The name of the restaurant is {self.name}.')
        print(f"The type of the restaurant is {self.type}.")
    def open_restaurant(self):
        print('the restaurant is opening.')
    '''my_restaurant = Restaurant('haidilao','hotpot')
    my_restaurant.number_served = 15
    print(f"{my_restaurant.number_served} people are served by {my_restaurant.name}")'''
    def set_number_served(self, number):
        self.number_served = number
        print(f'{self.number_served} is served.')
    def increment_number_served(self,people):
        self.number_served += people