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
            diffusion_result_encrypt = _diffusion_encrypt_shift(confussion_result_encrypt, char_key)
            
            operator = confussion_result_encrypt # cambiar a diffusion_result_encrypt

        binary_array_result.append(operator)
    result_encrypt = _diffusion_encrypt_rotation(binary_array_result, key)
    base64_result = base64.b64encode(str(result_encrypt).encode('utf-8'))
    
    return binary_array_result, base64_result

def _confussion_encrypt(binary_char1: str, binary_char2: str, key_length: int):
    xor_result = xor_binary_values(binary_char1, binary_char2)
    multiplied_result = multiply_binary(xor_result, key_length)
    return multiplied_result
        

def _diffusion_encrypt_shift(binary_msg: str, charKey: str):

    shifts = 0
    nrs = str(int(charKey, 2)) # Number of right shifts 
    for i in range(0, len(nrs)):
        if (shifts <= 7):
            shifts += int(nrs[i])
    shifts = (shifts - 8 if shifts >= 9 else shifts)
    
    shifted_binary = shift(binary_msg, shifts)
    #print("----------")
    #print(shifts)
    #print(binary_msg)
    #print(shifted_binary)
    #print("----------")
    return shifted_binary

def _diffusion_encrypt_rotation(binary_msg: str, key: str):
    
    # We get all concatenation of values
    fullBinaryMsg = list(''.join(binary_msg))

    n = str(int(transform_char_to_ascii(key[-1]),2))
    kn = 0
    kn = sum(int(n[i]) for i in range(len(n)))
    kn = int(str(kn)[-1])

    
    rotatedBinary = (fullBinaryMsg[kn:] + fullBinaryMsg[:kn])
    result = ''.join(rotatedBinary)
    print(result, fullBinaryMsg)
    return result

# Shift right
def shift(binary_string: str, shifts: int):
    #print(binary_string)
    binary_string = str(format(int(binary_string,2), '08b'))
    
    #print(binary_string)
    firstPart = binary_string[:shifts]
    rest = binary_string[shifts:]
    shifted = rest + firstPart
    #print(shifted)
    
    shifted_binary = bin(int(shifted, 2))
    #print(shifted_binary)
    return shifted_binary