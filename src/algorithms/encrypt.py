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
            difussion_result_encrypt = _difussion_encrypt(confussion_result_encrypt, char_key)
            
            operator = difussion_result_encrypt

        binary_array_result.append(operator)
        
    base64_result = base64.b64encode(str(binary_array_result).encode('utf-8'))
    
    return binary_array_result, base64_result

def _confussion_encrypt(binary_char1: str, binary_char2: str, key_length: int):
    xor_result = xor_binary_values(binary_char1, binary_char2)
    multiplied_result = multiply_binary(xor_result, key_length)
    return multiplied_result
        

def _difussion_encrypt(binary_msg: str, key_char: str):
    # Number of right shifts 
    nrs = str(int(key_char, 2))
    shifts = 0
    
    for i in range(0, len(nrs)):
        if (shifts <= 7):
            shifts += int(nrs[i])
    # (if n < 0 then shifting by 2 positions)
    shifts = (shifts if shifts <= 8 else shifts - 8)

    # Convert binary string to an integer
    decimal_number = int(binary_msg, 2)
    # Perform a bitwise shift right operation 
    shifted_decimal = decimal_number >> shifts
    # Convert the shifted decimal number back to a binary string
    shifted_binary = bin(shifted_decimal)

    print(shifts)
    print(binary_msg)
    print(shifted_binary)
    print("")
    return shifted_binary