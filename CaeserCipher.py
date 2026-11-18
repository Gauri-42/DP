
# Caesar Cipher Algorithm

def encryption(text, key):
    cipher = ""

    for char in text:
        if char.isupper():
            cipher += chr((ord(char) - 65 + key) % 26 + 65)

        elif char.islower():
            cipher += chr((ord(char) - 97 + key) % 26 + 97)

        else:
            cipher += char

    return cipher


def decryption(text, key):
    plain = ""

    for char in text:
        if char.isupper():
            plain += chr((ord(char) - 65 - key) % 26 + 65)

        elif char.islower():
            plain += chr((ord(char) - 97 - key) % 26 + 97)

        else:
            plain += char

    return plain


text = input("Enter the text: ")
key = int(input("Enter the key: "))

cipher = encryption(text, key)

print("Original Text:", text)
print("Encrypted Text:", cipher)
print("Decrypted Text:", decryption(cipher, key))
