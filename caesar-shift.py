import string 

def create_substitution_string(n):
    encoding = dict()
    decoding = dict()
    alphabet_size = len(string.ascii_uppercase)
    
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        shifted_letter = string.ascii_uppercase[(i*n)%alphabet_size]
        encoding[letter] = shifted_letter
        decoding[shifted_letter] = letter
        
    return encoding, decoding 

def encode(message, subst):
    cipher = ""
    
    for letter in message:
        if letter in subst:
            cipher += subst[letter]
        else:
            cipher += letter 
            
    return cipher 

def decode(message, subst):
    return encode(message, subst)