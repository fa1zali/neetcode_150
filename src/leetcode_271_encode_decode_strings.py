# Design an algorith to encode a list of strings to a string. 
# The encoded string is then sent over the network and is decoded back to the original list of strings

def encoder(arr):
    if len(arr) == 0:
        return False
    else:
        str = ''
        for elm in arr:
            str += elm + chr(258)
    
    encoded_str = str[0:-1]
    return encoded_str


def decoder(str):
    decoded_lst = []
    start_index = 0
    delimiter = chr(258)
    delimiter_len = len(delimiter)
    
    for i in range(len(str) - delimiter_len + 1):

        if str[i:i + delimiter_len] == delimiter:
            substring = str[start_index:i]
            decoded_lst.append(substring)
            
            start_index = i + delimiter_len
            
    decoded_lst.append(str[start_index:])
    
    return decoded_lst


encoded_val = encoder(arr = ['ab', 'b', 'xy', 'nin'])
print(encoded_val)
if encoded_val != False:
    decoded_val = decoder(encoded_val)
    print(decoded_val)