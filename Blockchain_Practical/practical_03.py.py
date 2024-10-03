import hashlib

# Initializing string
string = "SIPNA COET"

# SHA256
result = hashlib.sha256(string.encode())
print("The hexadecimal equivalent of SHA256 is:")
print(result.hexdigest())

print("\r")  # Line break

# SHA384
result = hashlib.sha384(string.encode())
print("The hexadecimal equivalent of SHA384 is:")
print(result.hexdigest())

print("\r")  # Line break

# SHA224
result = hashlib.sha224(string.encode())
print("The hexadecimal equivalent of SHA224 is:")
print(result.hexdigest())

print("\r")  # Line break

# SHA512
result = hashlib.sha512(string.encode())
print("The hexadecimal equivalent of SHA512 is:")
print(result.hexdigest())

print("\r")  # Line break

# SHA1
result = hashlib.sha1(string.encode())
print("The hexadecimal equivalent of SHA1 is:")
print(result.hexdigest())
