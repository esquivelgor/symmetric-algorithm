from src.utils.binary import transform_char_to_ascii
import base64


def encrypt_message(plain_text: str, key: str) -> str:
    return _confussion(plain_text, key)

def _multiply_binary(binary_result: str, key_length: str):
    key_binary = bin(key_length)
    multiplied_result = int(binary_result, 2) * int(key_binary, 2)
    return bin(multiplied_result)

def _confussion(plain_text: str, key: str) -> str:
    
    key_ascii = []
    plain_text_ascii = []
    binary_array_result = []
    
    for char in key:
        key_ascii.append(transform_char_to_ascii(char))
        
    for char in plain_text:
        plain_text_ascii.append(transform_char_to_ascii(char))
    
    for char_key in key_ascii:
        operator = char_key
        for char_message in plain_text_ascii:
            xor_result = _xor_binary_values(operator, char_message)
            multiplied_result = _multiply_binary(xor_result, len(key))
            operator = multiplied_result
        
        binary_array_result.append(multiplied_result)
        
    base64_result = base64.b64encode(str(binary_array_result).encode('utf-8'))
    
    return binary_array_result, base64_result

def _xor_binary_values(binary_char1: str, binary_char2: str) -> str:
        """
        XOR operation between 2 strings values in binary format.
        Exmaple:
        binary_char1 = "0b01000001"
        binary_char2 = "0b01000010"
        result = "0b00000011"
        """
        
        # binary_char1 = f"{ord(char1):08b}"
        # binary_char2 = f"{ord(char2):08b}"
        
        xor_decimal = int(binary_char1, 2) ^ int(binary_char2, 2)
        
        xor_result_binary = bin(xor_decimal)
        
        return xor_result_binary

def _difussion(plain_text: str, key: str) -> str:
    """
    TODO
    """
    pass