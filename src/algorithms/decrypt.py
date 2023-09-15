import base64

def decrypt_message(encrypted_message: str, key: str) -> str:

    binary_array = base64.b64decode(encrypted_message).decode('utf-8')
    
    print(binary_array)
    
    return "TODO: Implement this endpoint."

def rollback_confussion(encrypted_message: str, key: str) -> str:
    """
    TODO
    """
    pass

def rollback_diffusion(encrypted_message: str, key: str) -> str:
    """
    TODO
    """
    pass