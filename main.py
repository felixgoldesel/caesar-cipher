from string import ascii_lowercase
from string import ascii_uppercase

print("Geheimtext: ")
ciphertext = input()
decrypted = ""
#value_counter = 1
counter = 0

#while counter <= 26:
for i in ciphertext:
    value_uppercase = ord(i)
    if 65 <= ord(i) < 90:
        decrypted += chr(value_uppercase + 1)
    elif ord(i) >= 90:
        value_uppercase = 65
        decrypted += chr(value_uppercase)

    ciphertext = decrypted
print(decrypted)
#    counter += 1


git remote add origin https://github.com/felixgoldesel/caesar-cipher.git
git branch -M main
git push -u origin main

