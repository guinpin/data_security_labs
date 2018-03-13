#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:31:58 2018

@author: dell
"""
import  math
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def RSA_encr(message, p, q):
    plain_text = []
    
    for letter in message:
        ind = alphabet.index(letter)
        plain_text.append(ind + 1)
        
    n = p * q
    
    phi_n = (p - 1) * (q - 1)
    
    e = 2
    while gcd(phi_n, e) != 1:
        if e > 1 and e < phi_n:
            e += 1
                
    d = math.pow(e, -1) % phi_n
    
    PU = [e, n]
    print("Public key: ", PU)
        
    C = []
    for M in plain_text:
        c = int(math.pow(M, e) % n)
        C.append(c)
        
    return C

message = ['H', 'I']
p = 3
q = 5 
message_string = ''.join(message)
print("Message", message_string)
result = RSA_encr(message, p, q)
print("Encrypted message", result)