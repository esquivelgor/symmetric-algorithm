from src.utils.binary import transform_char_to_ascii, multiply_binary, xor_binary_values
import base64


def encrypt_message(plain_text: str, key: str) -> str:
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
            confussion_result_encrypt = _confussion_encrypt(operator, char_key, len(key))
            # TODO: Call Difussion decrypt here with the result of the confussion
            # Then assign the result of the difussion to the operator
            operator = confussion_result_encrypt
            
        binary_array_result.append(confussion_result_encrypt)
        
    base64_result = base64.b64encode(str(binary_array_result).encode('utf-8'))
    
    return binary_array_result, base64_result

def _confussion_encrypt(binary_char1: str, binary_char2: str, key_length: int):
    xor_result = xor_binary_values(binary_char1, binary_char2)
    multiplied_result = multiply_binary(xor_result, key_length)
    
    return multiplied_result
        

def _difussion_encrypt(plain_text: str, key: str) -> str:
    """
    TODO
    """
    pass