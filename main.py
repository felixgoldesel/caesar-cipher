option = input("Entschlüsseln [1] oder Verschlüsseln [2]: ")
#LPUMBLOYBUN PU KPL RYFWAVNYHWOPL


def decrypt(ciphertext):

    counter = 1
    decrypted = ""
    ciphertext = ciphertext.upper()

    while counter <= 26:
        for i in ciphertext:
            if ord(i) == 32:
                decrypted += " "
            elif ord(i) == 65:
                value_uppercase = 90
                decrypted += chr(value_uppercase)
            elif 65 < ord(i) <= 90:
                decrypted += chr(ord(i) - 1)

        ciphertext = decrypted
        print(decrypted + " KEY: " + str(counter))
        decrypted = ""
        counter += 1


def encrypt(plaintext, key):

    encrypted = ""
    plaintext = plaintext.upper()

    for i in plaintext:
        if ord(i) == 32:
            encrypted += " "
        elif ord(i) + int(key) <= 90:
            encrypted += chr(ord(i) + int(key))
        elif ord(i) + int(key) > 90:
            value = (ord(i) + int(key)) - 90
            encrypted += chr(64 + value)
    print(encrypted)


if option == "1":
    decrypt(input("Geheimtext: "))
elif option == "2":
    encrypt(input("Text: "), input("Key: "))
