def make_car(factory,type,**car_info):
    car_info['factory'] = factory
    car_info['type'] = type
    return car_info
car = make_car('ford','10005',color = 'red',tow_package = True)
print(car)