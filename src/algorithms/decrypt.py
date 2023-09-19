import base64
from src.utils.binary import transform_char_to_ascii, divide_binary, xor_binary_values, transform_ascii_to_char


def decrypt_message(encrypted_message: str, key: str) -> str:

    
    binary_array_string = base64.b64decode(encrypted_message).decode('utf-8')
    reversed_key = key[::-1]
    
    # transform string in formart of array to list of strings
    binary_array = binary_array_string.replace("[", "").replace("]", "").replace("'", "").split(", ")
    
    key_ascii = []
    binary_ascii = []
    
    for char in reversed_key:
        key_ascii.append(transform_char_to_ascii(char))
    
    for binary in binary_array:
        operator = binary
        for char_key in key_ascii:
            confussion_decrypt_result = _confussion_decrypt(operator, char_key, len(key))
            
            operator = confussion_decrypt_result # debe de ir diffusion_decrypt_result

        binary_ascii.append(operator)   
    result_decrypt = _diffusion_encrypt_transposition(binary_ascii, key)
    
    decrypted_plain_text = ""
    for binary_ascii in result_decrypt:
        decrypted_plain_text += transform_ascii_to_char(binary_ascii)
    
    
    return result_decrypt, decrypted_plain_text
    

def _confussion_decrypt(binary_char1: str, binary_char2: str, key_length: int) -> str:
    divided_result = divide_binary(binary_char1, key_length)        
    xor_result = xor_binary_values(binary_char2, divided_result)
    
    return xor_result

def _diffusion_encrypt_transposition(binary_msg: str, key: str):
    
    kn = len(key)
    result = binary_msg[kn:] + binary_msg[:kn]
    
    return result

def _diffusion_decrypt_shift(encrypted_message: str, charKey: str):
    
    shifts = 0
    nrs = str(int(charKey, 2)) # Number of left shifts 
    for i in range(0, len(nrs)):
        if (shifts <= 7):
            shifts += int(nrs[i])
    shifts = (shifts - 8 if shifts >= 9 else shifts)

    binary_msg = shift(encrypted_message, shifts)
    return encrypted_message

# Shift right (decrypt)
def shift(binary_string: str, shifts: int):

    return 1

