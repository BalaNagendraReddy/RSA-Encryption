from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
import base64

# Generate 1024-bit RSA key pair (private + public key)
keyPair = RSA.generate(bits=1024)


# Sign the message using the PKCS#1 v1.5 signature scheme (RSASP1)
msg = b'A message for signing'
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(keyPair)
signature = signer.sign(hash)

print("Signature in raw:", signature)
print("Signature in binascii:", binascii.hexlify(signature))
print("Signature:", base64.b64encode(signature).decode('ascii'))

# Verify valid PKCS#1 v1.5 signature (RSAVP1)
msg = b'A message for signing'
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(keyPair)
try:
    signer.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")

# Verify invalid PKCS#1 v1.5 signature (RSAVP1)
msg = b'A tampered message'
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(keyPair)
try:
    signer.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")
