import pymongo
from time import sleep
from utils import bcolors, get_login_data, print_banner, clear, print_options, raise_error
import os

client = pymongo.MongoClient(os.environ['MONGODB_ATLAS'])
mydb = client["RPSCluster"]


def script():
    while True:
        try:
            clear()
            print_banner("SELECT AN OPTION")
            print_options(["1. Register", "2. Login"])
            option = input("Your option is: ")
            assert option.isnumeric(), "Select a valid option"
            option = int(option)
            assert option == 1 or option == 2, "Select a valid option"
            register() if option == 1 else login()
        except AssertionError as ve:
            print("")
            print(ve.args)
            sleep(1)
            script()


def main_interface(user_information):
    while True:
        try:
            clear()
            print_banner("Your notes:")
            notes = mydb["notes"].find({"author": user_information["_id"]})
            index = 0
            for note in notes:
                print(f'{index}. {note["text"]}')
                index += 1
            print_banner("Select what you want to do")
            print_options(
                ["1. Add a new note", "2. Delete a note", "3. Logout"])
            option = int(input("Your selection is: "))
            assert option == 1 or option == 2 or option == 3, "Select a valid option"
            if option == 1:
                add_note(user_information)
            if option == 2:
                delete_note(user_information, index)
            if option == 3:
                logout()
        except AssertionError as ve:
            print("")
            print(ve.args[0])
            sleep(1)
            main_interface(user_information)


def register():
    data = get_login_data()
    response = mydb["users"].find_one({"username": data["username"]})
    assert response == None, "User already exists!"
    try:
        mydb["users"].insert_one(data)
        print("Registered correctly!!")
        sleep(1)
    except:
        raise_error()


def login():
    data = get_login_data()
    response = mydb["users"].find_one({"username": data["username"]})
    if not response:
        raise AssertionError("Username doesn't exist, try again")
    assert response["password"] == data["password"], "Incorrect password, please try again!"
    print(f'{bcolors.OKGREEN}Logged in successfully!{bcolors.ENDC}')
    sleep(1)
    main_interface(response)


def add_note(user_information):
    id = user_information["_id"]
    clear()
    print("Note:")
    text = str(input(""))
    assert len(list(text)) > 5, "Notes must have at least 5 characters"
    try:
        mydb["notes"].insert_one({
            "author": id,
            "text": text
        })
        print(f'{bcolors.OKGREEN}Note added!!{bcolors.ENDC}')
        sleep(1)
        main_interface(user_information)
    except:
        raise_error()


def delete_note(user_information, amount_of_notes):
    id = user_information["_id"]
    print("")
    print("Which note do you wanna delete(index)?")
    option = int(input(""))
    notes = mydb["notes"].find({"author": user_information["_id"]})
    notes = [note for note in notes]
    assert option <= amount_of_notes, "That note doesn't exist"
    try:
        mydb["notes"].delete_one({
            "author": id,
            "text": notes[option]["text"]
        })
        print(f'{bcolors.OKGREEN}Note deleted!!{bcolors.ENDC}')
        sleep(1)
        main_interface(user_information)
    except:
        raise_error()


def logout():
    print(f'')
    print(f'{bcolors.OKGREEN}Logged out succesfully{bcolors.ENDC}')
    sleep(1)
    script()
