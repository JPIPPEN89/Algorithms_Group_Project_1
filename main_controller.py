import random
import math

from main import generate_prime


class Main_Controller:


    def generate_public_key(self):
        pass


        #Fermat test is to make sure that we catch composite numbers
        #Will implement by generating primes in a while loop until both p and q pass the fermat test###########
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

    def e(self):
        p,q = generate_prime()
        phi = (p-1) * (q-1)
        e = random.randint(2, phi)
        while math.gcd(e, phi) != 1:
            e = random.randint(2, phi)
        return e

    # Example usage
