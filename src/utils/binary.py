def transform_char_to_ascii(char: str) -> str:
    """
    Transform a char to its ASCII representation.
    Returning the binary in bin python type.
    """
    byte_array_char = char.encode()
    return bin(int.from_bytes(byte_array_char, byteorder='big'))

def multiply_binary(binary_result: str, key_length: str):
    key_binary = bin(key_length)
    multiplied_result = int(binary_result, 2) * int(key_binary, 2)
    return bin(multiplied_result)

def xor_binary_values(binary_char1: str, binary_char2: str) -> str:
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