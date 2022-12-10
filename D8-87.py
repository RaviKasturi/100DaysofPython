# https://replit.com/@appbrewery/caesar-cipher-3-start#main.py

from caesar_cipher import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, shift):
    shift = shift % 26
    if direction == 'encode':
        encoded_text = ""
        for i in range(len(text)):
            if text[i] in alphabet:
                encoded_text += text[i].replace(text[i], alphabet[(alphabet.index(text[i]) + shift) % 26])
        print(encoded_text)
    elif direction == 'decode':
        decoded_text = ""
        for i in range(len(text)):
            if text[i] in alphabet:
                decoded_text += text[i].replace(text[i], alphabet[(alphabet.index(text[i]) - shift) % 26])
        print(decoded_text)
    else:
        print('Incorrect cipher mechanism selected.')


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(direction=direction, text=text, shift=shift)
