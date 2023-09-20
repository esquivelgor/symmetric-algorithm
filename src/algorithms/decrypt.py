import base64
from src.utils.binary import transform_char_to_ascii, divide_binary, xor_binary_values, transform_ascii_to_char, shift_left
from fastapi import HTTPException, status


def decrypt_message(encrypted_message: str, key: str) -> str:

    try:
        binary_array_string = base64.b64decode(encrypted_message).decode('utf-8')
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The encrypted is not a valid base64 string"
        )
        
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
            # diffusion_decrypt_result = _diffusion_decrypt_shift(confussion_decrypt_result, char_key)
            operator = confussion_decrypt_result ## cambiar a diffusion_decrypt

        binary_ascii.append(operator)   
         
    result_decrypt = _diffusion_decrypt_transposition(binary_ascii, key)
    
    decrypted_plain_text = ""
    for binary_ascii in result_decrypt:
        decrypted_plain_text += transform_ascii_to_char(binary_ascii)
    
    return result_decrypt, decrypted_plain_text
    

def _confussion_decrypt(binary_char1: str, binary_char2: str, key_length: int) -> str:
    divided_result = divide_binary(binary_char1, key_length)        
    xor_result = xor_binary_values(binary_char2, divided_result)
    
    return xor_result

def _diffusion_decrypt_transposition(binary_msg: str, key: str):
    
    kn = len(key)
    result = binary_msg[kn:] + binary_msg[:kn]
    
    return result

def _diffusion_decrypt_shift(binary_msg: str, charKey: str):
    decimal_ascii_code = str(int(charKey, 2))
    
    number_of_shifts = sum([int(i) for i in decimal_ascii_code])

    number_of_shifts = (number_of_shifts - 8 if number_of_shifts >= 9 else number_of_shifts)
    
    # print("number_of_shifts: ", number_of_shifts)
    
    return shift_left(binary_msg, number_of_shifts)

    # shifts = 0
    # nrs = str(int(charKey, 2)) # Number of shifts 
    # for i in range(0, len(nrs)):
    #     if (shifts <= 7):
    #         shifts += int(nrs[i])
    # shifts = (shifts - 8 if shifts >= 9 else shifts)

    # binary_msg = shift(encrypted_message, shifts)
    # return binary_msg

