import random
import math




class Main_Controller:

    # Fermat test is to make sure that we catch composite numbers
    # Will implement by generating primes in a while loop until both p and q pass the fermat test###########
    # n will be p first and then when that is generated q will be ready

    def fermat_test(self,n):
        test = True

        for i in range(0,100):
            a = random.randrange(2, n - 1)
            g = math.gcd(a,n)
            if g != 1:
                test = False
                break
            if pow(a, n - 1, n) != 1:
                test = False
                break

        return test

    def generate_prime(self):

        while True:
            p = random.randint(1000000, 1003000)
            q = random.randint(1000000, 1003000)
            if p != q:
                if self.fermat_test(p) and self.fermat_test(q):
                    return p, q


    def generate_public_key(self,p,q):
        n = p*q
        phi = (p-1)*(q-1)

        e = random.randint(2, phi)

        while math.gcd(e, phi) != 1:
            e = random.randint(2, phi)

        return e,phi

    def extended_gcd(self,a, b):

        if b == 0:
            return (1, 0, a)

        (x, y, d) = self.extended_gcd(b, a % b)

        return y, x - a // b * y, d

    def generate_private_key(self,e,phi):

        x = self.extended_gcd(e, phi)
        d = x[0] % phi

        return d



    def encrypt_message(self, e, n):
        message = input('Type your short message:  ')
        message = message.upper()
        st = "Here is the ciphered text: "
        msg = ""

        for x in message:

            x = pow(ord(x),e,n)

            msg += str(x) + " "

        msg = msg.strip()
        print(st + msg)

        return msg

    def decrypt_message(self, msg, d, n):
        parts = msg.split()
        plaintext = ""
        for s in parts:
            m = pow(int(s), d, n)
            plaintext += chr(m)
        print("Here is the deciphered text: " + plaintext)
        return plaintext

