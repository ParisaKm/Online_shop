import csv
import hashlib
import re
import logging
import tkinter
from tkinter import messagebox
import os
import ast

logger = logging.getLogger("ShopManager")
logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s' \n",
                    datefmt='%d-%b-%y %H:%M:%S')

"""this is successfully good project"""


def menu():
    print("you are sign in as manager")
    ShopManagerMenu.alert_of_ending_stocks()
    print(
        "add_goods=1\nstocks=2\nalert_of_ending_stocks=3\nfactor_search=4\nshow_customers_factors=5\nshow_customers_specifications=6\ncustomers_bank=7\nsign_out=8\nexit=0\n")
    n = 1
    while n != 0:
        n = int(input("choose the option : "))
        if n == 1:
            ShopManagerMenu.add()
        elif n == 2:
            ShopManagerMenu.show_stocks()
        elif n == 3:
            ShopManagerMenu.alert_of_ending_stocks()
        elif n == 4:
            ShopManagerMenu.factor_search(search_for=int(input("user phone num")))
        elif n == 5:
            show_factors = ShopManagerMenu.show_customers_factors()
            print(show_factors)
        elif n == 6:
            ShopManagerMenu.show_customers_specifications()
        elif n == 7:
            ShopManagerMenu.customers_block()
        elif n == 8:
            menu()
        else:
            break


class ShopManager:
    def __init__(self, shop_name=''):
        self.shop_name = shop_name

    @classmethod
    def sign_in(cls):
        username = input("enter phone_num as username : ")
        x = re.findall("09\d{9}", username)
        if [username] != x:
            print("wrong")
        password = input("enter password : ")
        pass_word = hashlib.sha256(password.encode('utf-8')).hexdigest()
        with open("ShopManager_Info.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            find = False
            for row in reader:
                if username == row['username']:
                    if pass_word == row['password']:
                        print("signed in")
                        print(menu())
                    else:
                        break

    @classmethod
    def sign_up(cls) -> object:
        for i in range(1):
            username = input("enter phone_num as username : ")
            x = re.findall("09\d{9}", username)
            if [username] != x:
                print("Wrong number!")

            elif [username] == x:
                with open("ShopManager_Info.csv", "r") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if username != row["username"]:
                            break
                        else:
                            print("you were applied!")
            else:
                break
            shop_name = input("Enter your shop name : ")
            password = input("enter password: ")
            password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            with open('test.csv', 'a') as csvfile:
                columns = ['username', 'password', 'shop_name']
                writer = csv.DictWriter(csvfile, fieldnames=columns)
                if csvfile.tell() == 0:
                    writer.writeheader()
                writer.writerows([{'username': username, 'password': password, 'shop_name': shop_name}])
                print("you signed in successfully")


class ShopManagerMenu:

    @classmethod
    def add(cls):
        username = input("enter phone_num as username : ")
        with open("ShopManager_Info.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if username == row['username']:
                    p_barcode = int(input("enter barcode"))
                    p_price = int(input("Enter price"))
                    p_name = input("Enter name")
                    p_num_stocks = int(input("Enter number of this product"))
                    exp_date = int(input("Enter Expire date"))
                    # try:
                    #     if isinstance(exp_date, int):
                    #         return False
                    # except:
                    #     logging.error()

                    with open('ShopManager_Info.csv', 'a') as csvfile:
                        columns = ['username', 'p_barcode', 'p_price', 'p_brand', 'p_name', 'p_num_stocks', 'exp_date']
                        writer = csv.DictWriter(csvfile, fieldnames=columns)
                        writer.writerows([{'username': username, 'p_barcode': p_barcode, 'p_price': p_price,
                                           'p_name': p_name, 'p_num_stocks': p_num_stocks,
                                           'exp_date': exp_date}])
                        print("you add product successfully")
                n = 1
                while n != 0:
                    n = int(input("enter 1 to continue : "))
                    if n == 1:
                        continue
                    else:
                        ShopManager.sign_in()
        return cls()

    """بعد از ورود مشخصات کاال های موجود،مدیر فروشگاه باید بتواند لیستی از کاالهای موجود 
در فروشگاه و مشخصات و تعداد هریک را مشاهده کند"""

    @classmethod
    def show_stocks(cls):
        username = input("enter phone_num as username : ")
        with open("ShopManager_Info.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if username == row['username']:
                    print(row)

    @classmethod
    def alert_of_ending_stocks(cls):
        username = input("enter phone_num as username : ")
        with open("ShopManager_Info.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if username == row['username']:
                    find = int(row['p_num_stocks'])
                    findd = row['p_name']
                    if find <= 5:
                        # This code is to hide the main tkinter window
                        root = tkinter.Tk()
                        root.withdraw()
                        a = find
                        # Message Box
                        messagebox.showinfo(a, f"{a} of {findd} is remained")
                else:
                    print(menu())

    @classmethod
    def factor_search(cls, search_for):
        if search_for:
            result = ShopManagerMenu.f_reader()
        for factor in result:
            cls.print_dict(factor)


    @classmethod
    def f_reader(cls):
        with open('factor.csv', 'r') as myfile:
            reader = csv.DictReader(myfile)
            return list(reader)


    """ مشاهده لیست مشخصات کلیه مشتری ها"""

    @classmethod
    def show_customers_factors(cls):
        with open('factor.csv', 'r') as myfile:
            reader = csv.DictReader(myfile)
            for row in reader:
                print(row)

    @classmethod
    def show_customers_specifications(cls):
        with open("UserInfo.csv", 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row['name']
                family = row['family']
                phone_num = row['username']
                print(name, family, phone_num)

    @classmethod
    def customers_block(cls, search_for):
        # username = input("phone_num :")
        if search_for:
            with open("ShopManager_Info.csv", "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if search_for == row['username']:
                        user = 1
                    if user is not None:
                        # This code is to hide the main tkinter window
                        root = tkinter.Tk()
                        root.withdraw()
                        a = user
                        # Message Box
                        messagebox.showinfo(a, f" {user} you are blocked")
                        break


class Customer:
    def __init__(self, name='', family=''):
        self.name = name
        self.family = family

    @classmethod
    def sign_up(cls):
        for i in range(2):
            username = input("enter phone_num as username : ")
            x = re.findall("09\d{9}", username)
            if [username] != x:
                print("Wrong number!")

            elif [username] == x:
                with open("UserInfo.csv", "r") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if username != row["username"]:
                            print(username)
                        else:
                            print("you were applied!")
                            break
            else:
                break
        name = input("name : ")
        family = input("family")
        password = input("enter password: ")
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        with open('test.csv', 'a') as csvfile:
            columns = ['username', 'password']
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerows([{'username': username, 'password': password, 'name': name, 'family': family}])
            print("you signed in successfully")

    @classmethod
    def sign_in(cls):
        for i in range(3):
            username = input("enter phone_num as username : ")
            x = re.findall("09\d{9}", username)
            if [username] != x:
                print("wrong")
            else:
                break
        password = input("enter password: ")
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        with open("UserInfo.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            find = False
            for row in reader:
                if username == row['username']:
                    find = True
                    if password == row['password']:
                        print("Correct")
                    else:
                        print("Wrong")
            if not find:
                print("There is not such a username!")


def test_module():
    print('this is from file_handler.py')
