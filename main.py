import main_controller as mc

def main_menu():
    #print("RSA keys have been generated.")

    key = str(input("Please select your user type:\n"
          "\t1. A public User\n"
          "\t2. The owner of the keys\n"
          "\t3. Exit Program"))

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

    functions = {"1" : send_encrypt, "2" : dig_sign, "3": 'Have a great day!'}

    if key == '3':
        print(functions['3'])
        return

    return functions[key] ()

def key_owner():
    key = str(input("As the owner of the keys, what would you like to do?\n"
                    "\t1. Decrypt a received message\n"
                    "\t2. Digitally sign a message\n"
                    "\t3. Exit"))

    functions = {"1": decrypt_message, "2": digital_sign, "3": 'Have a great day!'}

    if key == '3':
        print(functions['3'])
        return

    return functions[key]()

if __name__ == "__main__":
    main_menu()