import random

# Function that generates the key
def keyGen():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    key = random.sample(alphabet, len(alphabet))
    return key

#function that takes a message and "cleans" it.
def clean_string(s):
    # Remove all non-alphanumeric characters
    s = ''.join(c for c in s if c.isalnum())
    # Convert all characters to lowercase
    s = s.lower()
    # Remove all spaces
    s = ''.join(s)
    return s

def cipher(message, alpha, key):
    # Create a dictionary that maps the alphabet to the key
    cipher_dict = dict(zip(alpha, key))
    # Use the dictionary to translate the message
    cipher_message = ''.join(cipher_dict.get(c, c) for c in message)
    return cipher_message

def decipher(message, alpha, key):
    # Create a dictionary that maps the key to the alphabet
    decipher_dict = dict(zip(key, alpha))
    # Use the dictionary to translate the message
    decipher_message = ''.join(decipher_dict.get(c, c) for c in message)
    return decipher_message

def main():
    # Generate the key
    key = keyGen()
    # Define the alphabet
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    # Get the message from the user
    message = input('Enter a message: ')
    # Clean the message
    message = clean_string(message)
    # Encrypt the message
    cipher_message = cipher(message, alpha, key)
    print('Encrypted message:', cipher_message)
    # Decrypt the message
    decipher_message = decipher(cipher_message, alpha, key)
    print('Decrypted message:', decipher_message)

if __name__ == '__main__':
    main()
