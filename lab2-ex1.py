#!/usr/bin/env python3
alphabet_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def caesar_cipher(mes, shift):
    message = list(mes)
    for i in range(len(message)):
        if message[i] in alphabet_low:
            index = alphabet_low.index(message[i])
            message[i] = alphabet_low[(index + shift)%26]
        if message[i] in alphabet_up:
            index = alphabet_up.index(message[i])
            message[i] = alphabet_up[(index + shift)%26]
    
    message = ''.join(message)

    return(message)
            
mes = "Hello"
key = 3

print("Message: ", mes)
print("Key: ", key)
print("Ciphertext: ", str(caesar_cipher(mes, key)))

