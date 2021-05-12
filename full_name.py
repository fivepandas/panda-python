first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
full_name = f"Hell0, {full_name.title()}!"
print(full_name)#f 字符串是是python 3.6 引入的，之前的版本需要使用format
full_name = "{} {}".format(first_name, last_name)
print("Python")
print("\tPython")
print("Languages:\nPython\nC")