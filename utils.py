from os import system

# Asks for the login information and returns the response 
def get_login_data():
    clear()
    print("Introduce your username:")
    email = input("")
    assert len(email) > 5, "Username length must be longer than 5 characters"
    clear()
    print("Introduce your password:")
    password = input("")
    assert len(password) > 5, "Password length must be longer than 5 characters"
    mydict = { "username": email, "password": password }
    return mydict

# Prints a banner with the text assigned 
def print_banner(text):
    print(f'{bcolors.OKBLUE}------------------------{bcolors.ENDC}')
    print(f'{bcolors.OKBLUE}{text}:{bcolors.ENDC}')
    print(f'{bcolors.OKBLUE}------------------------{bcolors.ENDC}')

# Cleans the console 
def clear():
    system("cls")

# Prints the options to be selected, receives an array with them
def print_options(options):
    for option in options:
        print(option)

def raise_error():
    raise AssertionError(f'{bcolors.FAIL}Something went wrong, try again!{bcolors.ENDC}')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'