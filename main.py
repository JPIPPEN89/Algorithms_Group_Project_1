import main_controller as mc

def main_menu():
    print("RSA keys have been generated.")
    print("Please select your user type:\n"
          "\t1. A public User\n"
          "\t2. The owner of the keys\n"
          "\t3. Exit Program")
    key = str(input())

    functions = {"1": public_user, "2": owner, "3": 'Have a great day!'}

    if key == '3':
        print(functions['3'])
        return

    return functions[key]

