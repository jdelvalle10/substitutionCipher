# Substitution Cipher
This Python script implements a simple substitution cipher, which is a method of encrypting plaintext by replacing each letter with another letter. The substitution is determined by a randomly generated key.

## Usage
Key Generation: Upon running the script, a new key will be generated randomly. The key is a permutation of the alphabet, ensuring each letter is mapped to a different letter.

Message Input: After the key is generated, the user is prompted to enter a message to be encrypted.

Encryption: The entered message is then cleaned, removing non-alphanumeric characters, converting all characters to lowercase, and eliminating spaces. The cleaned message is then encrypted using the generated key.

Decryption: After encryption, the encrypted message is displayed. The script then decrypts this message using the same key, revealing the original plaintext message.

## Functions
keyGen(): Generates a random key by shuffling the alphabet.

clean_string(s): Cleans the input string by removing non-alphanumeric characters, converting characters to lowercase, and eliminating spaces.

cipher(message, alpha, key): Encrypts the message using the substitution cipher.

decipher(message, alpha, key): Decrypts the message using the same key.

## Running the Script
To run the script, execute it in a Python environment. Ensure that Python 3.x is installed on your system.

bash
Copy code
python substitution_cipher.py
Requirements
Python 3.x
Author
Written by [Mr D.]

## License
This project is licensed under the MIT License - see the LICENSE file for details.
