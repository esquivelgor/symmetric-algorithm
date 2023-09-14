
def encrypt_message(plain_text: str, key: str) -> str:
    """
    Encrypts a message using the RSA algorithm.
    """
    return _confussion(plain_text, key)

def _xor_strings(str1, str2):
    
    def _xor_binary_values(char1, char2):
        binary_char1 = f"{ord(char1):08b}"
        binary_char2 = f"{ord(char2):08b}"

        result = ""

        for bit1, bit2 in zip(binary_char1, binary_char2):
            xor_result = "1" if bit1 != bit2 else "0"
            result += xor_result

        return result
    
    result = ""
    key_length = len(str1)

    for i, char2 in enumerate(str2):
        char1 = str1[i % key_length]
        xor_result = _xor_binary_values(char1, char2)
        result += xor_result

    return result 

def _confussion(plain_text: str, key: str) -> str:
    
    def _multiply_binary_result(binary_result, key_length):
        multiplied_result = binary_result * key_length
        return multiplied_result
    
    xor_result = _xor_strings(key, plain_text)  # Assuming you have the xor_strings function from the previous response
    key_length = len(key)
    multiplied_result = _multiply_binary_result(xor_result, key_length)

    return multiplied_result



def _difussion(plain_text: str, key: str) -> str:
    """
    TODO
    """
    pass