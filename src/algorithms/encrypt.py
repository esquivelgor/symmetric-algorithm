from src.utils.binary import transform_char_to_ascii, multiply_binary, xor_binary_values, shift_right
import base64

def encrypt_message(plain_text: str, key: str) -> str:
    key_ascii = []
    plain_text_ascii = []
    binary_array_result = []
    
    for char in key:
        key_ascii.append(transform_char_to_ascii(char))
        
    for char in plain_text:
        plain_text_ascii.append(transform_char_to_ascii(char))
    
    for char_message in plain_text_ascii:
        operator = char_message
        for char_key in key_ascii:
            confussion_result_encrypt = _confussion_encrypt(operator, char_key, len(key))
            # diffusion_result_encrypt = _diffusion_encrypt_shift(operator, char_key)
            operator = confussion_result_encrypt # cambiar a diffusion_result_encrypt

        binary_array_result.append(operator)
    
    # Apply transposition layer encryption
    result_encrypt = _diffusion_encrypt_transposition(binary_array_result, key) 

    base64_result = base64.b64encode(str(result_encrypt).encode('utf-8'))
    
    return result_encrypt, base64_result

def _confussion_encrypt(binary_char1: str, binary_char2: str, key_length: int):
    xor_result = xor_binary_values(binary_char1, binary_char2)
    multiplied_result = multiply_binary(xor_result, key_length)
    return multiplied_result

def _diffusion_encrypt_transposition(binary_msg: str, key: str):
    
    kn = len(key)
    result = binary_msg[-kn:] + binary_msg[:-kn]
    
    return result

def _diffusion_encrypt_shift(binary_msg, charKey: str):

    decimal_ascii_code = str(int(charKey, 2))

    number_of_shifts = sum([int(i) for i in decimal_ascii_code])
    
    number_of_shifts = (number_of_shifts - 8 if number_of_shifts >= 9 else number_of_shifts)
    
    # print("number_of_shifts: ", number_of_shifts)
    
    return shift_right(binary_msg, number_of_shifts)

    # shifts = 0
    # nrs = str(int(charKey, 2)) # Number of shifts 
    # for i in range(0, len(nrs)):
    #     if (shifts <= 7):
    #         shifts += int(nrs[i])
    # shifts = (shifts - 8 if shifts >= 9 else shifts)
    
    # shifted_binary = shift(binary_msg, shifts)
    # return shifted_binary
    
    