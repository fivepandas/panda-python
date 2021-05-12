favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()},thank you for taking the poll.")
sorted(favorite_languages.keys())
print(sorted(favorite_languages))
print("the following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
for language in set(favorite_languages.values()):
    print(language.title())
test_name = ['jen','sarah','andy','ross']
for name in favorite_languages.keys():
    if name in test_name:
        print(f"{name.title()}, thank you for your cooperation")
    else:
        print(f"{name.title()}, you need take a test")