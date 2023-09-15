import base64
from src.utils.binary import transform_char_to_ascii, divide_binary, xor_binary_values, transform_ascii_to_char


def decrypt_message(encrypted_message: str, key: str) -> str:

    
    binary_array_string = base64.b64decode(encrypted_message).decode('utf-8')
    reversed_key = key[::-1]
    
    # transform string in formart of array to list of strings
    binary_array = binary_array_string.replace("[", "").replace("]", "").replace("'", "").split(", ")
    
    
    return _confussion_decrypt(binary_array, reversed_key)
    

def _confussion_decrypt(binary_array: list[str], key: str) -> str:

    key_ascii = []
    decrypted_in_binary_ascii = []
    
    for char in key:
        key_ascii.append(transform_char_to_ascii(char))
    
    for binary in binary_array:
        operator = binary
        for char_key in key_ascii:
            
            divided_result = divide_binary(operator, len(key))
            
            xor_result = xor_binary_values(char_key, divided_result)
            operator = xor_result
        
        decrypted_in_binary_ascii.append(operator)    
    
    decrypted_plain_text = ""
    for binary_ascii in decrypted_in_binary_ascii:
        decrypted_plain_text += transform_ascii_to_char(binary_ascii)
    
    
    return decrypted_in_binary_ascii, decrypted_plain_text

def rollback_diffusion(encrypted_message: str, key: str) -> str:
    """
    TODO
    """
    pass