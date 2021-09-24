import csv
from csv import DictWriter
import hashlib
input re

"""this is successfully good project"""


class ShopManager:

    @classmethod
    def sign_in(cls):
        username = regex(09\d{09})
        username = username
        password = input("enter password : ")
        Password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        cls.name = input("Enter your name : ")
        cls.last_name = input("Enter your last name : ")
        with open("ShopManager_Info", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            find = False

            for row in reader:
                if username == row['username']:
                    find = True
                    if Password == row['password']:
                        print("Correct")
                    else:
                        print("Wrong")
            if not find:
                print("There is not such a username!")

    @classmethod
    def sign_up(cls):
        username = input("enter phone_num as username : ")
        try:
            if len(username) != 11:
                return True
        except Exception:
            print("Wrong username!")
        username = username
        password = input("enter password: ")
        Password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        with open('ShopManager_Info.csv', 'a') as csvfile:
            columns = ['username', 'password']
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            if csvfile.tell() == 0:
                writer.writeheader()
            # list_username = []
            # if username not in list_username:
            #     list_username.append(u)
            writer.writerows([{'username': username, 'password': Password}])
            print("you signed in successfully")


def sign_up():
    username = input("enter phone_num as username: ")
    try:
        if len(username) != 11:
            return True
    except:
        print("Wrong username!")
    username = username
    password = input("enter password: ")
    Password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    with open('UserInfo.csv', 'a') as csvfile:
        columns = ['username', 'password']
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerows([{'username': username, 'password': Password}])
        print("you signed in successfully")


def sign_in():
    username = input("enter username: ")
    password = input("enter password: ")
    Password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    with open("UserInfo.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        find = False
        for row in reader:
            if username == row['username']:
                find = True
                if Password == row['password']:
                    print("Correct")
                else:
                    print("Wrong")
        if not find:
            print("There is not such a username!")


def test_module():
    print('this is from file_handler.py')

# class FileHandler:
#     def __init__(self, file_path='run.csv'):
#         self.file_path = file_path

# def read_file(self):
#     with open(self.file_path, 'r') as myfile:
#         reader = csv.DictReader(myfile)
#         return list(reader)

# def add_to_file(self, new_value):
# if isinstance(new_value, dict):
#     fields = new_value.keys()
#     new_value = [new_value]
# elif isinstance(new_value, list):
#     fields = new_value[0].keys()
#
# with open(self.file_path, 'a') as myfile:
#     fields = ""
#     writer = DictWriter(myfile, fieldnames=fields)
#     if myfile.tell() == 0:
#         writer.writeheader()
#     writer.writerows(new_value)
