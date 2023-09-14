
def encrypt_message(plain_text: str, key: str) -> str:
    """
    Encrypts a message using the RSA algorithm.
    """
    return confussion(plain_text, key)

def xor_binary_values(char1, char2):
    binary_char1 = f"{ord(char1):08b}"
    binary_char2 = f"{ord(char2):08b}"

    result = ""

    for bit1, bit2 in zip(binary_char1, binary_char2):
        xor_result = "1" if bit1 != bit2 else "0"
        result += xor_result

    return result

def xor_strings(str1, str2):
    result = ""
    key_length = len(str1)

    for i, char2 in enumerate(str2):
        char1 = str1[i % key_length]
        xor_result = xor_binary_values(char1, char2)
        result += xor_result

    return result 


def multiply_binary_result(binary_result, key_length):
    multiplied_result = binary_result * key_length
    return multiplied_result

def confussion(plain_text: str, key: str) -> str:
    
    xor_result = xor_strings(key, plain_text)  # Assuming you have the xor_strings function from the previous response
    key_length = len(key)
    multiplied_result = multiply_binary_result(xor_result, key_length)

    return multiplied_result
