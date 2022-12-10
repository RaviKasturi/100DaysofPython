# https://replit.com/@appbrewery/caesar-cipher-1-start#main.py

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    shift = shift % 26
    encoded_text = ""
    helper = []
    for i in range(len(text)):
        if text[i] in alphabet:
            helper += text[i]
            encoded_text += text[i].replace(text[i], alphabet[(alphabet.index(text[i])+shift) % 26])
    print(encoded_text)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == 'encode':
    encrypt(text=text, shift=shift)
