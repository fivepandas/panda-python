guests_dinner = ['Lao zi','Wu Zetian','Yuan Tiangang']
message = "Could you please have dinner with me?"
print(f'{guests_dinner[0]},{message}')
print(f'{guests_dinner[1]},{message}')
print(f'{guests_dinner[2]},{message}')

print(f"{guests_dinner[1]} can't attend the meeting.")
guests_dinner[1] = "Si Maqian"
print(f'{guests_dinner[0]},{message}')
print(f'{guests_dinner[1]},{message}')
print(f'{guests_dinner[2]},{message}')
guests_dinner.append
guests_dinner.insert(0,"Li Shiming")
guests_dinner.insert(1,"Zhu Yuanzhang")
guests_dinner.append("Zhao KuangYing")
print(f'{guests_dinner[0]},{message}')
print(f'{guests_dinner[1]},{message}')
print(f'{guests_dinner[2]},{message}')
print(f'{guests_dinner[3]},{message}')
print(f'{guests_dinner[4]},{message}')
print(f'{guests_dinner[5]},{message}')

print("Sorry,I just can invite two guest to have a dinner with me.")
g1 = guests_dinner.pop()
print(f"Sorry,{g1}you don't need to come.")
g2 = guests_dinner.pop()
print(f"Sorry,{g2}you don't need to come.")
g3 = guests_dinner.pop()
print(f"Sorry,{g3}you don't need to come.")
g4 = guests_dinner.pop()
print(f"Sorry,{g4}you don't need to come.")
print(f"{guests_dinner[0]},{message}")
print(f"{guests_dinner[1]},{message}")
del guests_dinner[0]
del guests_dinner[0]
print(guests_dinner)