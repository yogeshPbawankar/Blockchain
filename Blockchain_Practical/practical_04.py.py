import math

def gcd(a, b):
    """Compute the Greatest Common Divisor using Euclid's algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find the multiplicative inverse."""
    if a == 0:
        return (b, 0, 1)
    else:
        gcd_val, x, y = extended_gcd(b % a, a)
        return (gcd_val, y - (b // a) * x, x)

def multiplicative_inverse(e, phi):
    """Find the multiplicative inverse of e modulo phi."""
    gcd_val, x, _ = extended_gcd(e, phi)
    if gcd_val != 1:
        return None  # Inverse doesn't exist
    else:
        return x % phi

def generate_keys():
    """Generate RSA public and private keys with user inputs."""
    print("PLEASE ENTER THE 'p' AND 'q' VALUES BELOW:")
    
    # Input prime numbers p and q from the user
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    
    # Compute n and Euler's Totient
    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"RSA Modulus (n) is: {n}")
    print(f"Eulers Toitent (r) is: {phi}")
    
    # Set e manually as 999
    e = 999
    print(f"The value of e is: {e}")
    
    # Show steps of Euclid's algorithm
    print("\nEUCLID'S ALGORITHM:")
    a, b = e, phi
    while b != 0:
        quotient = a // b
        remainder = a % b
        print(f"{a} = {quotient} * {b} + {remainder}")
        a, b = b, remainder
    
    print("END OF THE STEPS USED TO ACHIEVE EUCLID'S ALGORITHM.\n")
    
    # Compute d (private key exponent)
    d = multiplicative_inverse(e, phi)
    
    print("EUCLID'S EXTENDED ALGORITHM:")
    gcd_val, s, _ = extended_gcd(e, phi)
    print(f"1 = {e} * ({s}) + {phi} * (some_value)")
    if s < 0:
        s = s % phi
        print(f"s = {s} (since s < 0, s = s mod r)")
    print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
    
    print(f"The value of d is: {d}")
    
    public_key = (e, n)
    private_key = (d, n)
    
    print(f"Private Key is: {private_key}")
    print(f"Public Key is: {public_key}")
    
    return public_key, private_key

def encrypt(public_key, plaintext):
    """Encrypt the plaintext using the public key."""
    e, n = public_key
    ciphertext = []
    for char in plaintext:
        m = ord(char) - 65  # Simple conversion of characters (A=0, B=1, ..., Z=25)
        c = pow(m, e, n)
        ciphertext.append(c)
    return ciphertext

def decrypt(private_key, ciphertext):
    """Decrypt the ciphertext using the private key."""
    d, n = private_key
    decrypted_message = []
    for c in ciphertext:
        m = pow(c, d, n)
        decrypted_message.append(chr(m + 65))  # Convert back to uppercase letter
    return ''.join(decrypted_message)

def main():
    print("RSA ENCRYPTOR/DECRYPTOR")
    
    # Generate keys with user input
    public_key, private_key = generate_keys()
    
    # Input message to encrypt
    message = input("\nWhat would you like encrypted or decrypted? (Enter an uppercase message for encryption): ")
    print(f"Your message is: {message}")
    
    # Ask user whether to encrypt or decrypt
    print("\nType '1' for encryption and '2' for decryption.")
    choice = input()
    
    if choice == '1':
        encrypted_msg = encrypt(public_key, message)
        print(f"Your encrypted message is: {encrypted_msg}")
    elif choice == '2':
        # For decryption, the user must provide the ciphertext
        ciphertext = list(map(int, input("Enter the encrypted message (comma-separated numbers): ").split(',')))
        print(f"Your decrypted message is: {decrypt(private_key, ciphertext)}")
    else:
        print("Invalid option.")
    
    print("\nThank you for using the RSA Encryptor. Goodbye!")

if __name__ == "__main__":
    main()
