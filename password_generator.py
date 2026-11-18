
import random

# Read dictionary file
file = open(r"DP\dictionary.txt", "r")

words = []

for line in file:
    word = line.strip()
    if word != "":
        words.append(word)

file.close()

# Take number of words
n = int(input("Enter number of words: "))

# Select random words
selected_words = random.sample(words, n)

# All possible separators
separators = "!@#$%^&*_-+0123456789"

password = ""

# Join words using random separators
for i in range(n):
    password = password + selected_words[i]

    if i < n - 1:
        separator = random.choice(separators)
        password = password + separator

print("Generated Password:", password)
