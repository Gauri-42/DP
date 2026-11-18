
import hashlib
import requests

# Function to check whether password is leaked
def check_password(password):

    # Generate SHA-1 hash
    hash_value = hashlib.sha1(password.encode()).hexdigest().upper()

    # Divide hash into prefix and suffix
    prefix = hash_value[:5]
    suffix = hash_value[5:]

    # Send prefix to API
    url = "https://api.pwnedpasswords.com/range/" + prefix

    response = requests.get(url)

    # Check all returned hashes
    for line in response.text.splitlines():

        parts = line.split(":")
        returned_hash = parts[0]
        count = parts[1]

        if returned_hash == suffix:
            return count

    return 0


# Read username and password file
file = open("username_password.txt", "r")

for line in file:

    line = line.strip()

    if line == "":
        continue

    username, password = line.split(",")

    count = check_password(password)

    if int(count) > 0:
        print(username, "- Password leaked", count, "times")
    else:
        print(username, "- Password not leaked")

file.close()
