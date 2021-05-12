class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaurant(self):
        print(f'The name of the restaurant is {self.name}.')
        print(f"The type of the restaurant is {self.type}.")
    def open_restaurant(self):
        print('the restaurant is opening.')
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []
    def describe_flavors(self):
        flas = self.flavors
        for fla in flas:
            print(fla)

Ice_1 = IceCreamStand('DQ',"desert")
Ice_1.flavors = ['strawbbery','banana','yogurt']
Ice_1.describe_flavors()