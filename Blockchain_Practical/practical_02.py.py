def diffie_hellman(p, g, a, b):
    A = pow(g, a, p)
    B = pow(g, b, p)
    
    shared_secret_a = pow(B, a, p)
    shared_secret_b = pow(A, b, p)
    if shared_secret_b == shared_secret_a:
        print("Secret key for the Alice is : ",shared_secret_a)
        print("Secret key for the Bob is : ",shared_secret_b)
    else:
        return None
            
p = int(input("The value of P: "))
g = int(input("The value of G: "))
a = int(input("The private key a for Alice: "))
b = int(input("The private key b for Bob: "))


key = diffie_hellman(p, g, a, b)

