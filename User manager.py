#Project 2: User Manager

import random
import os

users={}

def load_user_data():
#module to check if a file or directory exists
    if os.path.exists('user_data.txt'):
        user_data = open('user_data.txt')
        for line in user_data:
            user = line.split(':')

#split returns a list so I can add the key and the value this way
            if len(user) == 2:
                users[user[0]] = user[1].strip()
    else:
        user_data = open('user_data.txt','w')


def save_user_data():
    user_data = open('user_data.txt','w')

    for key in users:
        user_data.write(key)
        user_data.write(':')
        user_data.write(users[key])
        user_data.write('\n')

    user_data.close()


def create_username():
    print("Enter your name: ")
    name = input()

    print("Enter your last name: ")
    last_name = input()

    number = random.randint(1000,9999)
    last_name = last_name.lower()
    name=name.lower()

#map and str to convert characters into a list of string type to join them all
    username="".join(map(str,[name[0], last_name, number]))
    return username


def get_username():
    print("Enter your username: ")
    username = input()

    return username


def test_valid_password(password, ban_characters='!@$:?'):
    min_length = 7
    password_check = True

    if (len(password) >= min_length) and (password_check == True):
        for character in password:
            if character in ban_characters:
                password_check = False
                break

    else:
        password_check = False

    return password_check


def encrypted_password(password):
#swap first and last letter then put into new string variable
    first_string=password[0]
    last_string=password[-1]
    password=password[1:-1]
    final_password="".join([last_string,password,first_string])


#looping through the string variable to change characters then put it into another string variable
    encrypted_passw =[]
    for letter in final_password:

        if(letter =='a'):
            encrypted_passw += '@'

        elif(letter =='S'):
            encrypted_passw += '$'

        elif(letter == 'i'):
            encrypted_passw += '!'

        elif(letter == 'J'):
            encrypted_passw += '?'

        else:
            encrypted_passw += letter

    encrypted_passw = "".join(encrypted_passw)
    return encrypted_passw


def get_password():
    count=5
    while count > 0:
        print("Enter a Password: ")
        password = input()

        if (test_valid_password(password)):
            print("Re-enter Password: ")
            re_password = input()

            if (re_password == password):
                return password

            else:
                count-=1
                print("Passwords do not match\n")

        else:
            count-=1
            print("Pease enter a valid password, minimum 7 length, no special characters(!@$:?)\n")

    return None

def write_to_log(username,status):
    log = open('log.txt','a')
    log.write(username)
    log.write("::")
    log.write(status)
    log.write('\n')
    log.close()

def check_user(username,password):
    if username in users:
        dictionary_password = users[username]
        encrypted_pass = encrypted_password(password)

        if dictionary_password == encrypted_pass:
            return True

        else:
            return False
    else:
        return False


def update_password(username):
    password = get_password()
    encryp_password = encrypted_password(password)
    users[username] = encryp_password

    save_user_data()
    print("\nPassword was succesfuly updated.\n")

    write_to_log(username,'UPDATE')


def add_user():
    user = create_username()
    passw = get_password()
    encrypt_passw = encrypted_password(passw)

    users[user] = encrypt_passw
    save_user_data()
    write_to_log(user,'NEW USER')


def print_log():
    log = open('log.txt')
    logs = log.read()

    print(logs)
    log.close()


def display_main_menu():
    print("\n ___________________________________________________\n"
          "|                                                   |\n"
          "|                                                   |\n"
          "|    Welcome, login or create an user to begin.     |\n"
          "|                                                   |\n"
          "|___________________________________________________|\n")


    print("\n1. Login.\n"
           "2. Create New User.\n"
           "3. Quit.\n")

def display_user_menu(user):
    print("\n ___________________________________\n"
          "|                                   |\n"
          "       Welcome,", user,"            \n"
          "|___________________________________|\n")


    print("\n1. Print Logs.\n"
           "2. Update a password.\n"
           "3. Quit.\n")


def main():
    load_user_data()
    main_loop = True

    while main_loop:
        display_main_menu()
        selection = input()

#login
        if selection == '1':
            user = get_username()
            password = get_password()
            check = check_user(user,password)

#login succesfull
            if check:
                write_to_log(user,"OK")
                display_user_menu(user)
                login_selection = input()

                if login_selection == '1':
                    print_log()

                elif login_selection == '2':
                    update_password(user)

                elif login_selection == '3':
                    print("\n ___________________________\n"
                            "|                           |\n"
                            "|     Thank you, Goodbye    |\n"
                            "|___________________________|\n")
                    save_user_data()
                    main_loop = False


#login failed
            else:
                print("\n     ## Incorrect username or password ##      ")
                write_to_log(user, "BAD PASS")

#create account
        elif selection == '2':
            add_user()

#quit
        elif selection == '3':
            print("\n ___________________________\n"
                  "|                           |\n"
                  "|     Thank you, Goodbye    |\n"
                  "|___________________________|\n")
            save_user_data()
            main_loop = False

main()

