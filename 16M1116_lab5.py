#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 11:45:32 2018

@author: dell
"""
def encrypt(p, g, a, b):
    
    A = (g**a)%p
    B = (g**b)%p
    K1 = (A**b)%p
    K2 = (B**a)%p
    
    if K1==K2:
        return K1
    
def encrypt2(plaintext,K):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    plaintext = plaintext.upper()
    cip_index = ""
    for ind,val in enumerate(plaintext):
        cip_index += str(alphabet[int(int(alphabet.index(val)+1)+K)%36-1])
    
    return cip_index

plaintext = "helloIamcommingon23offebruary"
print("Plain text:", plaintext.upper())

p = 23
g = 5
a = 6
b = 15

K = encrypt(p, g, a, b)
print("Value of K:", K)

print("Ciphertext which is sent by party A:",encrypt2(plaintext, K))