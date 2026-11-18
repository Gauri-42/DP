
# Traditional Rail Fence Cipher

def encryption(text, rails):
    matrix = [['' for i in range(len(text))] for j in range(rails)]

    row = 0
    direction = 1

    for col in range(len(text)):
        matrix[row][col] = text[col]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    cipher = ""

    for i in range(rails):
        for j in range(len(text)):
            cipher += matrix[i][j]

    return cipher


def decryption(cipher, rails):
    matrix = [['' for i in range(len(cipher))] for j in range(rails)]

    row = 0
    direction = 1

    # Mark zigzag positions
    for col in range(len(cipher)):
        matrix[row][col] = '*'

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    # Fill cipher characters row-wise
    index = 0

    for i in range(rails):
        for j in range(len(cipher)):
            if matrix[i][j] == '*':
                matrix[i][j] = cipher[index]
                index += 1

    # Read zigzag to get plaintext
    plain = ""
    row = 0
    direction = 1

    for col in range(len(cipher)):
        plain += matrix[row][col]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return plain


text = input("Enter the plaintext: ")
rails = int(input("Enter the number of rails: "))

cipher = encryption(text, rails)

print("Encrypted Text:", cipher)
print("Decrypted Text:", decryption(cipher, rails))
