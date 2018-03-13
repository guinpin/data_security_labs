#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

alphabet_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def hill_cipher(mes, key_matrix):
    result = ''
    message = list(mes)
    indexes = ""
    block_size = key_matrix.shape[0]
    for i in range(0, len(message), block_size):
        if (i + block_size) > len(message):
            for j in range(len(message), i + block_size):
                message.append('k')
        for j in range(i, i + block_size, 1):
            if message[j] in alphabet_low:
                index = alphabet_low.index(message[j])
                indexes = indexes + " " + str(index)
                P = np.matrix(indexes)
        indexes = ""
        C = np.matmul(key_matrix, P.transpose())
        for k in C:
            k = k%26
            result += alphabet_low[int(k)]
    return(result)
    
mes = "mississippi"
key = np.matrix('3 25; 24 17')

print("Message: ", mes)
print("Key: ", key)
print("Ciphertext: ", hill_cipher(mes, key))