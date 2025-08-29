# Vigenère Cipher in Python

This project implements the **Vigenère cipher**, a method of encrypting
and decrypting text using a keyword.

## 📖 How It Works

1.  Each letter of the message is shifted by a number of positions in
    the alphabet.
2.  The shift amount is determined by the corresponding letter in the
    keyword.
3.  The keyword repeats to match the length of the message.
4.  Non-letter characters (spaces, punctuation) are preserved as-is.

-   **Encryption**: Shift forward in the alphabet.
-   **Decryption**: Shift backward in the alphabet.

## 🚀 Usage

Run the program with:

``` bash
python vigenere.py
```

Example input inside the script:

``` python
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'
```

### Output:

    Encrypted text: mrttaqrhknsw ih puggrur
    Key: python

    Decrypted text: hellochatgpt my friend

## 🛠 Example Code

``` python
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)
```

## ✅ Example Usage

``` python
# Encrypt a message
encrypted = encrypt("hello world", "python")
print(encrypted)

# Decrypt it back
print(decrypt(encrypted, "python"))
```

------------------------------------------------------------------------

📌 This project is for **educational purposes only**.

