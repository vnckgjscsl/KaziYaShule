def caesar_cipher(msg: str, key: int) -> str:
    encrypted_msg = ""

    for letter in msg:
        new_letter = chr((ord(letter) + key) % 26)
        encrypted_msg += new_letter 

    return encrypted_msg

def undo_ceasar_cipher(encrypted_msg: str, key: int) -> str:
    unencrypted_msg = ""

    for letter in encrypted_msg:
        old_letter = chr((ord(letter) - k) % 26)
        unencrypted_msg += old_letter

    return unencrypted_msg
