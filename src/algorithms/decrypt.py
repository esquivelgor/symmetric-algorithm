import base64
from src.utils.binary import transform_char_to_ascii, divide_binary, xor_binary_values, transform_ascii_to_char


def decrypt_message(encrypted_message: str, key: str) -> str:

    
    binary_array_string = base64.b64decode(encrypted_message).decode('utf-8')
    reversed_key = key[::-1]
    
    # transform string in formart of array to list of strings
    binary_array = binary_array_string.replace("[", "").replace("]", "").replace("'", "").split(", ")
    
    key_ascii = []
    decrypted_in_binary_ascii = []
    
    for char in reversed_key:
        key_ascii.append(transform_char_to_ascii(char))
    
    for binary in binary_array:
        operator = binary
        for char_key in key_ascii:
            confussion_decrypt_result = _confussion_decrypt(operator, char_key, len(key))
            difussion_decrypt_result = _diffusion_decrypt(operator, char_key)
            
            operator = confussion_decrypt_result


        decrypted_in_binary_ascii.append(operator)    

    decrypted_plain_text = ""
    for binary_ascii in decrypted_in_binary_ascii:
        decrypted_plain_text += transform_ascii_to_char(binary_ascii)
    
    
    return decrypted_in_binary_ascii, decrypted_plain_text
    

def _confussion_decrypt(binary_char1: str, binary_char2: str, key_length: int) -> str:
    divided_result = divide_binary(binary_char1, key_length)        
    xor_result = xor_binary_values(binary_char2, divided_result)
    
    return xor_result

def _diffusion_decrypt(encrypted_message: str, key: str):
    # Number of left shifts
    nrs = str(int(key, 2))
    shifts = 0
    for i in range(0, len(nrs)):
        if (shifts <= 7):
            shifts += int(nrs[i])

    shifts = (shifts if shifts <= 8 else shifts - 8)

    decimal_number_shifted = int(encrypted_message, 2)
    
    decimal_number = decimal_number_shifted << shifts

    binary_msg = bin(decimal_number)
    print(shifts)
    print(encrypted_message)
    print(binary_msg)
    print("")
    return encrypted_message
