import logging
import hashlib
import csv
import re
import file_Handler
from file_Handler import ShopManagerMenu
from file_Handler import Customer

logger = logging.getLogger("ShopManager")
logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s' \n",
                    datefmt='%d-%b-%y %H:%M:%S')


class Person:

    def __init__(self, username='', password='', shop_name=None, name=None, family=None):
        self.shop_name = shop_name
        self.username = username
        self.password = password
        self.shop_name = shop_name
        self.name = name
        self.family = family

    @classmethod
    def sign_up(cls):
        customer_manager = int(input("manager=>1 or customer=>2 : "))
        """
        this section is for manager sign up
        """
        if customer_manager == 1:
            for i in range(2):
                username = input("enter phone_num as username : ")
                x = re.findall("09\d{9}", username)
                if [username] != x:
                    print("Wrong number!")

                elif [username] == x:
                    with open("userinfo.csv", "r") as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            if username == row['username'] and 'manager' != row['post']:
                                continue
                            else:
                                print("you were applied!")
                                logging.warning('you were applied!')
                                break
                else:
                    logging.warning('you were applied!')
                    break
            shop_name = input("Store name : ")
            password = input("enter password: ")
            hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            check_pass = input("re-enter password: ")
            hash_check_pass = hashlib.sha256(check_pass.encode('utf-8')).hexdigest()
            """check if password was true"""
            if hash_password == hash_check_pass:
                """check if client is customer or manager"""
                with open('userinfo.csv', 'a') as csvfile:
                    columns = ['username', 'password', 'post', 'name', 'family', 'store_name']
                    writer = csv.DictWriter(csvfile, fieldnames=columns)
                    if csvfile.tell() == 0:
                        writer.writeheader()
                    writer.writerows([{'username': username, 'password': hash_password, 'post': 'manager',
                                       'name': "            ", 'family': '            ', 'store_name': shop_name}])
                    print(f"you signed up successfully as manager")


        elif customer_manager == 2:
            """this section is for customer sign up"""
            for i in range(2):
                username = input("enter phone_num as username : ")
                x = re.findall("09\d{9}", username)
                if [username] != x:
                    print("Wrong number!")

                elif [username] == x:
                    with open("userinfo.csv", "r") as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            if username == row['username']:
                                if 'customer' != row['post']:
                                    print('you were applied try another number')
                                    break
                            if username == row['username']:
                                if 'customer' == row['post']:
                                    print('you were applied try another number')
                                    break
                            else:
                                break
            name = input("name : ")
            family = input("family")
            password = input("enter password: ")
            hash_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            check_pass = input("re-enter password: ")
            hash_check_pass = hashlib.sha256(check_pass.encode('utf-8')).hexdigest()
            """check if password was true"""
            if hash_password == hash_check_pass:
                password = hash_password
                """check if client is customer or manager"""
                with open('userinfo.csv', 'a', newline='') as csvfile:
                    columns = ['username', 'password', 'post', 'name', 'family', 'store_name']
                    writer = csv.DictWriter(csvfile, fieldnames=columns)
                    if csvfile.tell() == 0:
                        writer.writeheader()
                    writer.writerows([{'username': username, 'password': password, 'post': 'customer',
                                       'name': name, 'family': family}])
                    print("you signed in successfully")

        else:
            raise TypeError("this input is WRONG!")

    def sign_in(self, username, password):
        """this section is for customer sign in"""
        customer_manager = int(input("for sign in as manager=>1 or customer=>2 : "))
        for i in range(2):
            self.username = input("enter phone_num as username : ")
            x = re.findall("09\d{9}", self.username)
            if [self.username] != x:
                print("Wrong number!")
                continue
            elif [self.username] == x:
                break
        password = input("enter password : ")
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if customer_manager == 1:
            with open("userinfo.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if self.username == row['username']:
                        if self.password == row['password']:
                            if 'manager' == row['post']:
                                print("you signed in as manager")
                                print(file_Handler.manager_menu())
                            else:
                                break
        elif customer_manager == 2:
            with open("userinfo.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row1 in reader:
                    if self.username == row1['username'] and self.password == row1['password'] and 'customer' == row1['post']:
                        obj_c = file_Handler.Customer(row1['username'], row1['password'], row1['post'], row1['name'],
                                                      row1['family'])
                        obj_c.customer_menu()
                        print("you signed in as customer")
