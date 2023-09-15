def transform_char_to_ascii(char: str) -> str:
    """
    Transform a char to its ASCII representation.
    Returning the binary in bin python type.
    """
    byte_array_char = char.encode()
    return bin(int.from_bytes(byte_array_char, byteorder='big'))