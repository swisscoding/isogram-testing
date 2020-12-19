#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Check if a word is an isogram | ----\n", fg("red")))

word = input("Enter the word: ").lower()

def check(word):
    count = 0
    for i in word:
        if word.count(i) > 1:
            count += 1

    if count != 0:
        return stylize(f"\n> '{word}' is not an isogram.\n", fg("red"))
    else:
        return stylize(f"\n> '{word}' is an isogram.\n", fg("red"))

print(check(word))
