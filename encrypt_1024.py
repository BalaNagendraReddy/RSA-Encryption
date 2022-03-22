# Message encrypts with public key and decrypts with Private key.

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64decode
from base64 import b64encode

from keys_1024 import *


def rsa_encrypt(s):
    key = b64decode(a_public_key)
    key = RSA.importKey(key)
    cipher = PKCS1_v1_5.new(key)
    ciphertext = b64encode(cipher.encrypt(bytes(s, "utf-8")))
    print(ciphertext)
    return ciphertext


def rsa_decrypt(s):
    key = b64decode(a_private_key)
    key = RSA.importKey(key)

    cipher = PKCS1_v1_5.new(key)
    plaintext = cipher.decrypt(b64decode(s), b"Error while decrypting")
    print(plaintext.decode('utf-8'))
    return plaintext


if __name__ == "__main__":
    enc_msg = rsa_encrypt("Hello Nagendra")
    rsa_decrypt(enc_msg.decode("ascii"))
