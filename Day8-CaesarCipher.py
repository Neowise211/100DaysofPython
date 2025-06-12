alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text,shift):
    encrypted = ""
    enIndex = 0
    for i in text:
        enIndex = alphabet.index(i) + shift
        if enIndex > 26:
            enIndex -= 26
        encrypted += alphabet[enIndex]



def decrypt(encrypted,shift):
    decrypted = ""
    decIndex = 0

    for i in encrypted:
        decIndex = alphabet.index(i) - shift

        if decIndex < 0:
            decIndex += 26

        decrypted +=alphabet(decIndex)

        print(f"Here's your encrypted message: {decrypted}")


if direction == 'encode':
    encrypted = str(encrypt(text, shift))
    print(f"Here's your encrypted message: {encrypted}")

    act = str(input("Now do you want to decode it [yes/no]:  "))

    if act == 'yes':
        decrypted = str(decrypt(encrypted, shift))


if direction == 'decode':
    decrypt(encrypted,shift)