import numpy as np

def create_key(key):
    matrix = []
    for letter in key.upper():
        if letter not in matrix:
            matrix.append(letter)
            
    alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    for letter in alphabet:
        if letter not in matrix:
            matrix.append(letter)

    matrix_key = []
    
    for letter in range(5):
        matrix_key.append('')
    
    matrix_key = np.asarray(matrix)
    matrix_key = np.reshape(matrix_key, (5, 5))
    
    return matrix_key

def delete_double_letters(message):
    mess = []
    for letter in message:
        mess.append(letter)

    i = 0
    for e in range(int(len(mess)/2)):
        if mess[i] == mess[i+1]:
            mess[i+1] = 'X'
        i = i + 2
    i = 0
    
    changed_mes=[]
    
    for x in range(1,int(len(mess)/2+1)):
        changed_mes.append(mess[i:i+2])
        i = i + 2
    return changed_mes

def get_pos(matrix,symb):
    x = 0
    y = 0
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == symb:
                x = i
                y = j
    return x,y

def playfair_cipher(message, key):
    
    message=delete_double_letters(message)
    key_matrix=create_key(key)
    
    result = []
    
    for letter in message:
        x1,y1 = get_pos(key_matrix,letter[0])
        x2,y2 = get_pos(key_matrix,letter[1])
        
        if x1 == x2:
            if y1 == 4:
                y1 = -1
            if y2 == 4:
                y2 = -1
            result.append(key_matrix[x1][y1+1])
            result.append(key_matrix[x1][y2+1])
        
        elif y1 == y2:
            if x1 == 4:
                x1 = -1;
            if x2 == 4:
                x2 = -1;
            result.append(key_matrix[x1+1][y1])
            result.append(key_matrix[x2+1][y2])
        else:
            result.append(key_matrix[x1][y2])
            result.append(key_matrix[x2][y1])
            
    result = ''.join(result)
    
    return(result)
    
mes = "HAMMER"
key = "MONARCHY"

print("Message: ", mes)
print("Key: ", key)
print("Ciphertext: ", playfair_cipher(mes, key))
