def transform_char_to_ascii(char: str) -> str:
    """
    Transform a char to its ASCII representation.
    Returning the binary in bin python type.
    """
    byte_array_char = char.encode()
    return bin(int.from_bytes(byte_array_char, byteorder='big'))

def transform_ascii_to_char(ascii: str) -> str:
    """
    Transform a ASCII representation to its char.
    Returning the char in str python type.
    """
    byte_array_char = int(ascii, 2).to_bytes((int(ascii, 2).bit_length() + 7) // 8, 'big')
    return byte_array_char.decode()

def multiply_binary(binary_result: str, key_length: int):
    key_binary = bin(key_length)
    multiplied_result = int(binary_result, 2) * int(key_binary, 2)
    return bin(multiplied_result)

def divide_binary(binary_result: str, key_length: int) -> int:
    key_binary = bin(key_length)
    
    divided_result = int(binary_result, 2) // int(key_binary, 2)
    
    
    return bin(divided_result)
    
    # print("divided_result: ", bin(divided_result))
    
    # mod = int(binary_result, 2) % int(key_binary, 2)
    
    # multiplication = multiply_binary(bin(divided_result), key_length)
    

    # # this is multiplication + mod, both in bin representation
    # binary_result = int(multiplication, 2) + int(bin(mod), 2)
   
    # return bin(binary_result)

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

# TESTS
# Encrypt
# 00010010 x 1000 = 010010000 

# test 1
# Decrypt — Sí es reversible
# 010010000 ÷ 1000 = 00010010

# Multiplicacion:  0b10010000
# Division:  0b10010000

# print("Multiplicacion: ", multiply_binary("0b00010010", 8))
# print("Division: ", divide_binary("0b010010000", 8))
