# Write a program to create a dictionary of hindi words with value as their English translation. Provide user with an option to look it up!


my_dictionary = {
    'parhna':'to learn',
    'jana':'to go',
    'rona':'to weap',
    'hansna':'to laugh'
}

print("*** My Dicitonary contains following Hindi Words to look up their English meanings ***")
for i in my_dictionary.keys():
    print (i)

hindi_word = input("Please enter word to look up its meaning: ")
for i in my_dictionary.keys():
    if (hindi_word == i):
        print(f"Meaning of {hindi_word} is {my_dictionary[i]}")
        

