from Crypto.PublicKey import RSA

x = RSA.generate(1024)

s_key = x.export_key()  # the private key
g_key = x.publickey().export_key()  # the public key

# implement rsa asymmetric encryption and decryption
my_private_key = s_key  # the private key
my_public_key = g_key  # the public key
print(my_public_key)
print(my_private_key)