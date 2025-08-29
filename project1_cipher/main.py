text = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
text = 'mrttaqrhknsw ih puggrur'   # This is the encrypted message (ciphertext)
custom_key = 'python'             # The keyword used for encryption/decryption


def vigenere(message, key, direction=1):
    """
    General Vigenère cipher function.
    - If direction = 1 → ENCRYPTION
    - If direction = -1 → DECRYPTION
    """
    
    key_index = 0                             # Tracks the current position in the keyword
    alphabet = 'abcdefghijklmnopqrstuvwxyz'   # Define the allowed alphabet (lowercase only)
    final_message = ''                        # Store the resulting encrypted or decrypted text

    # Iterate through each character in the message (converted to lowercase for consistency)
    for char in message.lower():

        # If the character is NOT a letter (like spaces or punctuation), leave it unchanged
        if not char.isalpha():
            final_message += char

        else:
            # Pick the correct letter from the key
            # key_index % len(key) ensures the keyword "wraps around" when the message is longer
            key_char = key[key_index % len(key)]
            key_index += 1  # Move to the next position in the key for the next character

            # Determine the shift value based on the key character
            # e.g., if key_char = 'p' → offset = 15 (since 'p' is the 16th letter, zero-based index 15)
            offset = alphabet.index(key_char)

            # Find the numeric index of the current message character
            index = alphabet.find(char)

            # Apply the Vigenère formula:
            # Encryption → (index + offset) % 26
            # Decryption → (index - offset) % 26  (done by multiplying offset * direction, where direction = -1)
            new_index = (index + offset * direction) % len(alphabet)
