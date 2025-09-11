import random
import math

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

    # Example usage
