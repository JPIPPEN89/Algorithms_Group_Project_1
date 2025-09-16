import math
import random

#Creating a class so that i can save the current variables and transfer them through the functions I already built
class RSA:
    def __init__(self):
        self.p = None
        self.q = None
        self.n = None
        self.e = None
        self.phi = None
        self.d = None

    def generate_keys(self): #####################WORKING HERE
        self.p, self.q =

    def fermat_test(self, n):
        test = True

        for i in range(0, 100):
            a = random.randrange(2, n - 1)
            g = math.gcd(a, n)
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

    def generate_public_key(self, p, q):
        n = p * q
        phi = (p - 1) * (q - 1)

        e = random.randint(2, phi)

        while math.gcd(e, phi) != 1:
            e = random.randint(2, phi)

        return e, phi

    def extended_gcd(self, a, b):

        if b == 0:
            return (1, 0, a)

        (x, y, d) = self.extended_gcd(b, a % b)

        return y, x - a // b * y, d

    def generate_private_key(self, e, phi):

        x = self.extended_gcd(e, phi)
        d = x[0] % phi

        return d

    def encrypt_message(self, e, n):
        message = input('Type your short message:  ')
        message = message.upper()
        st = "Here is the ciphered text: "
        msg = ""

        for x in message:
            x = pow(ord(x), e, n)

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

    # attempt at generating and verifying digital signature
    def sign_message(self, message: str, d: int, n: int) -> int:
        # Converts message into a number
        m_int = 0
        for ch in message:
            m_int = m_int * 256 + ord(ch)

            if m_int >= n:
                signature = pow(m_int, d, n)
                print("Signature (int): "
                signature)
                return signature

    def verify_signature(self, message: str, signature: int, e: int, n: int) -> bool:
        m_int = 0
        for ch in message:
            m_int = m_int * 256 + ord(ch)

            m_prime = pow(signature, e, n)
            is_valid = (m_int == m_prime)

    print("Verification passed?", is_valid)
    return is_valid


def main_menu(key):

    #print("RSA keys have been generated.")

    functions = {"1": public_user, "2": key_owner, "3": 'Have a great day!'}

    if key == '3':
        print(functions['3'])
        return

    return functions[key] ()

def public_user():

    key = str(input("As a public user, what would you like to do?\n"
          "\t1. Send an encrypted message\n"
          "\t2. Authenticate a digital signature\n"
          "\t3. Exit"))

    functions = {"1" : lambda:[], "2" : dig_sign, "3": 'Have a great day!'}

    if key == '3':
        print(functions['3'])
        return

    return functions[key] ()

def key_owner():
    key = str(input("As the owner of the keys, what would you like to do?\n"
                    "\t1. Decrypt a received message\n"
                    "\t2. Digitally sign a message\n"
                    "\t3. Show the keys"
                    "\t4. Generating a new set of the keys"
                    "\t5. Exit"))

    functions = {"1": decrypt_message, "2": digital_sign, '3': display_keys,
                 '4': generate_keys, "5": 'Have a great day!'}

    if key == '5':
        print(functions['5'])
        return

    return functions[key]()





if __name__ == "__main__":
    choice = 0

    # while loop runs until exits, this will be entry point for the program
    while choice != 3:
        choice = input(("Please Select Your User Type: "
              "\t1. A public user\n"
              "\t2. The owner of the keys\n"
              "\t3. Exit Program"))
        main_menu(input)



        p,q = mc.Main_Controller().generate_prime()
        n = p*q
        e, phi = mc.Main_Controller().generate_public_key(p,q)
        message = mc.Main_Controller().encrypt_message(e,n)
        d = mc.Main_Controller().generate_private_key(e,phi)

        mc.Main_Controller().decrypt_message(message, d, n)

        print(d)