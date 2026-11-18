
import random

password = input("Enter 3-digit password: ")

start_digit = random.randint(0, 9)

attempts = 0
found = False

for digit in range(10):

    first_digit = (start_digit + digit) % 10

    for i in range(10):
        for j in range(10):

            guess = str(first_digit) + str(i) + str(j)

            attempts += 1

            print("Trying:", guess)

            if guess == password:
                print("Password found:", guess)
                found = True
                break

        if found:
            break

    if found:
        break

print("Starting digit:", start_digit)
print("Total attempts:", attempts)
