#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def rail_fence(mes, depth):
    result = ''
   
    matrix = [""] * depth
    
    layer = 0
    
    for character in mes:
        matrix[layer] += character
        if layer >= depth - 1:
            layer = 0
        else:
            layer += 1

    result = "".join(matrix)        
        
    return(result)
        
mes = "defendhim"
key = 3

print("Message: ", mes)
print("Key: ", key)
print("Ciphertext: ", rail_fence(mes, key))

