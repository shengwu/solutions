from string import ascii_lowercase

def decrypt_array(arr, key):
    """Expects an array of integers representing an encrypted message,
    and a key that's a string"""
    key_len = len(key)
    decrypted = []
    for i, byte in enumerate(arr):
        decrypted.append(byte ^ ord(key[i % key_len]))
    return ''.join(map(chr, decrypted))

with open('p059_cipher.txt') as f:
    encrypted = f.read()
    encrypted_bytes_as_ints = map(int, encrypted.split(','))
    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                message = decrypt_array(encrypted_bytes_as_ints, a+b+c)
                if 'the' in message and 'his' in message and 'not' in message:
                    print message
                    print sum(map(ord, message))
