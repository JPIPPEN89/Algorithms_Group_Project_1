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
        self.encrypted_message = []
        self.decrypted_message = False
        self.dig_signatures = []


# Fermat test to check for prime number
    def fermat_test(self, n):
        test = True

        for i in range(0, 100):
            a = random.randrange(2, n - 1)
            g = math.gcd(a, n)
            if g != 1:
                test = False
                break
                #Fermat's little theorem
            if pow(a, n - 1, n) != 1:
                test = False
                break

        return test

    def generate_prime(self):
        # We are using large random integers and running the fermats test
        # to ensure that they are as close to prime as the could be

        while True:
            self.p = random.randint(1000000, 1003000)
            self.q = random.randint(1000000, 1003000)
            if self.p != self.q:
                if self.fermat_test(self.p) and self.fermat_test(self.q):
                    return

    # Generating the public key
    def generate_public_key(self):
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        # Choose e so that 1 < e < phi and gcd(e, phi) = 1
        self.e = random.randint(2, self.phi)
        while math.gcd(self.e, self.phi) != 1:
            self.e = random.randint(2, self.phi)

# Euclid's Extended Algorithm
    def extended_gcd(self, a, b):

        if b == 0:
            return (1, 0, a)

        (x, y, d) = self.extended_gcd(b, a % b)

        return y, x - a // b * y, d

    #Generating the private key
    def generate_private_key(self):

        x = self.extended_gcd(self.e, self.phi)
        self.d = x[0] % self.phi

# Encrypting the message using public key
    def encrypt_message(self):
        msg = input('Type your short message:  ')
        msg = msg.upper()
        st = "Here is the ciphered text: "
        msg1 = ""

        # RSA encryption 
        for x in msg:
            x = pow(ord(x), self.e, self.n)

            msg1 += str(x) + " "

        msg1 = msg1.strip()
        print(st + msg1)

        self.encrypted_message.append(msg1)
        print("Message Encrypted and Sent")


# Decrypting the message using private key
    def decrypt_message(self):
        print("The following messages are available:")
        if len(self.encrypted_message) == 0:
            print("No messages to decrypt")
            return

        for m in self.encrypted_message:
            count = 1
            print(f"\t{count}.\t(length = {len(m)})")

        choice = int(input("Enter your choice: "))

        parts = self.encrypted_message[choice-1].split()
        # RSA decryption
        plaintext = ""
        for s in parts:
            m = pow(int(s), self.d, self.n)
            plaintext += chr(m)
        print("Here is the deciphered text: " + plaintext)
        self.decrypted_message = True

# Signing the message using private key
    def sign_message(self):
        if len(self.encrypted_message) == 0:
            print("There are no messages to sign.")
            return

        msg = input("Enter a message: ")
        sig_parts = []
        for ch in msg:
            sig_parts.append(str(pow(ord(ch), self.d, self.n)))
        sig = " ".join(sig_parts)
        self.dig_signatures.append((msg, sig))
        print("Message signed and sent.")

    # Verifying digital signature using public key
    def verify_signature(self, message, signature, e, n):

        if len(self.dig_signatures) == 0:
            print("There are no signature to authenticate.")
            return

        print("The following messages are available:")
        for i, (msg, sig) in enumerate(self.dig_signatures, start=1):
            print(f"{i}. {msg}")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice")
            return
        if not (1 <= choice <= len(self.dig_signatures)):
            print("Invalid choice")
            return

        msg, sig = self.dig_signatures[choice - 1]
        tokens = sig.split()
        if len(tokens) != len(msg):
            print("Signature is invalid.")
            return

        ok = True
        for ch, t in zip(msg, tokens):
            m_prime = pow(int(t), self.e, self.n)  # verify with public key
            if m_prime != ord(ch):
                ok = False
                break

        if ok:
            print("Signature is valid.")
        else:
            print("Signature is invalid.")

    # Displaying the key
    def display_keys(self):
        if not self.n and not self.d:
            print("No private keys")
        else:
            print (f"n = {self.n} d = {self.d}")


    # def main_menu(self, key):
    #
    #     #print("RSA keys have been generated.")
    #     key = str(key)
    #     functions = {"1": lambda:(self.public_user()), "2": lambda:(self.key_owner()), "3": 'Have a great day!'}
    #
    #     if key == '3':
    #         print(functions['3'])
    #         return
    #
    #     return functions[key]

    # Menu options for users
    def public_user(self):
        key = ""

        key = str(input("As a public user, what would you like to do?\n"
              "\t1. Send an encrypted message\n"
              "\t2. Authenticate a digital signature\n"
              "\t3. Exit\n"))

        if key == '1':
            self.encrypt_message()
        elif key ==2:
            self.sign_message(self.d, self.n)
        elif key == '3':
            return



# Menu options for the key owner
    def key_owner(self):
        key = str(input("As the owner of the keys, what would you like to do?\n"
                        "\t1. Decrypt a received message\n"
                        "\t2. Digitally sign a message\n"
                        "\t3. Show the keys\n"
                        "\t4. Generate a new set of the keys\n"
                        "\t5. Exit\n"))

        if key == '1':
            self.decrypt_message()
            return
        elif key == '2':
            self.sign_message()
            return
        elif key == '3':
            self.display_keys()
            return
        elif key == '4':
            self.generate_keys()
            print("Keys Generated")
            return
        elif key == '5':
            print('Have a great day!')
            return
        else:
            print('Invalid choice')
            return
# Generating a RSA key pair
    def generate_keys(self):
        self.generate_prime()
        self.generate_public_key()
        self.generate_private_key()

        print("RSA Keys Generated")


if __name__ == "__main__":
    choice = 0
    app = RSA()
    app.generate_keys()

    # while loop runs until exits, this will be entry point for the program
    #keys is the RSA class where keys and messages will be saved and altered
    while choice != '3':
        choice = input(("Please Select Your User Type:\n "
              "\t1. A public user\n"
              "\t2. The owner of the keys\n"
              "\t3. Exit Program\n"))

        if choice == '1':
            app.public_user()
        elif choice == '2':
            app.key_owner()
        else:
            print("Have a great day!")
            break



