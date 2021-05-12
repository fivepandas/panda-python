motorcycles = ["honda","yamaha",'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati' #这里需要注意的是这里是把第一个元素替换了，而不是增加了一个元素
print(motorcycles)
m="nihaoya"
print(m[0])
motorcycles.append('ducati')
print(motorcycles)
motorcycles = [] #创建空的列表

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0,'ducati')#这个时候所有的列表往后移了，在最前面加入了一个元素
print(motorcycles)
del motorcycles[0]#删除之后，列表已经变了，再输出列表名的时候已经删除了这个元素
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
last_owned = motorcycles.pop()
print(f"the last motorcycle I owned was a {last_owned.title()}")
motorcycles = ["honda","yamaha",'suzuki']
motorcycles.remove('honda')