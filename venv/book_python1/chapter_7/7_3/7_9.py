sandwich_orders = ["bacon",'pastrami',"cheese",'pastrami',"hot dog",'pastrami']
print("pastrami is sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)