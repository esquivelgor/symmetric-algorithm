from src.utils.binary import transform_char_to_ascii, multiply_binary, xor_binary_values
import base64


def encrypt_message(plain_text: str, key: str) -> str:
    return _confussion_encrypt(plain_text, key)

def _confussion_encrypt(plain_text: str, key: str) -> str:
        
    key_ascii = []
    plain_text_ascii = []
    binary_array_result = []
    
    for char in key:
        key_ascii.append(transform_char_to_ascii(char))
        
    for char in plain_text:
        plain_text_ascii.append(transform_char_to_ascii(char))
        
    # Uncomment this to see in the console the ORDER
    # in which the operations are being done
    # for char_message in plain_text:
    #     for key_char in key:
    #         print(char_message, key_char)
    
    for char_message in plain_text_ascii:
        operator = char_message
        for char_key in key_ascii:
            xor_result = xor_binary_values(operator, char_key)
            multiplied_result = multiply_binary(xor_result, len(key))
            operator = multiplied_result
            
        binary_array_result.append(multiplied_result)
        
    base64_result = base64.b64encode(str(binary_array_result).encode('utf-8'))
    
    return binary_array_result, base64_result

def _difussion(plain_text: str, key: str) -> str:
    """
    TODO
    """
    pass