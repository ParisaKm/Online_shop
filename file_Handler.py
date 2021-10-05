import csv
import logging
import tkinter
from tkinter import messagebox

logger = logging.getLogger("ShopManager")
logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s' \n",
                    datefmt='%d-%b-%y %H:%M:%S')

"""this is successfully good project"""


def manager_menu():
    ShopManagerMenu.alert_of_ending_stocks()
    print(
        "add_goods=1\nstocks=2\nalert_of_ending_stocks=3\nfactor_search=4\nshow_customers_factors=5\n"
        "show_customers_specifications=6\ncustomers_bank=7\nsign_out=8\nexit=0\n")
    n = 1
    while n != 0:
        n = int(input("choose the option : "))
        if n == 1:
            sm = ShopManagerMenu()
            sm.add('username')
            manager_menu()
        elif n == 2:
            ShopManagerMenu.show_stocks()
        elif n == 3:
            ShopManagerMenu.alert_of_ending_stocks()
        elif n == 4:
            ShopManagerMenu.factor_search(search_for=int(input("user phone num")))
        elif n == 5:
            print(ShopManagerMenu.show_customers_factors())

        elif n == 6:
            ShopManagerMenu.show_customers_specifications()
        elif n == 7:
            """# ShopManagerMenu.customers_block()"""
        elif n == 8:
            manager_menu()
        else:
            break


class ShopManagerMenu:
    def __init__(self, username='', password='', shop_name=None, name=None, family=None):
        self.shop_name = shop_name
        self.username = username
        self.password = password
        self.shop_name = shop_name
        self.name = name
        self.family = family

    @classmethod
    def add(cls):
        username = input("enter your phone number to add")
        with open("userinfo.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if username == row['username']:
                    if 'manager' == row['post']:
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
                            columns = ['username', 'p_barcode', 'p_price', 'p_brand', 'p_name', 'p_num_stocks',
                                       'exp_date']
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
                        pass
                        # ShopManager.sign_in()

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
                    print(manager_menu())

    @classmethod
    def factor_search(cls, search_for):
        if search_for:
            pass
            # result = ShopManagerMenu.f_reader()
        # for factor in result:
        #     cls.print_dict(factor)

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
    def __init__(self,username,password,post, name='', family='',store_name=None):
        self.name = name
        self.family = family
        self.post = post
        self.username = username
        self.password = password
        self.store_name = store_name
        # self.username = Customer.sign_in(username)

    """مشاهده فاکتور خریدهای پیشین"""

    def customer_menu(self):
        print(' 1 => show last factors \n'
              ' 2 => show list of stores \n'
              ' 3 => search for store \n'
              ' 4 => choose a store \n'
              ' 5 => visit list of products \n'
              ' 6 => search for a product \n'
              ' 7 => choose a product \n'
              ' 8 => visit pre factor \n'
              ' 9 => confirm or edit \n'
              ' 0 => exit from account')
        n = 10
        while n != 0:
            n = int(input("choose the option : "))
            if n == 1:
                self.see_last_factors()
            elif n == 2:
                self.see_stores()
            elif n==3:
                self.search_for_stores()
            elif n==4:
                self.choose_for_stores()
            elif n==5:
                self.see_products()
            elif n==6:
                self.choose_products_and_add()
            else:
                break


    def see_last_factors(self):
        with open("factor.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if self.username == row['username']:
                    print(row)

    """نمایش لیستی از فروشگاه ها"""

    def see_stores(self):
        with open("userinfo.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if "manager" == row['post']:
                    print(row['store_name'], end='\n')

    """
    جستجوی فروشگاه
    مشتری می تواند در میان لیست نام فروشگاه ها جست و جو کند و در صورت فعال بودن 
اقدام به خرید کند.در صورتی که مشتری نامی خارج از لیست وارد کند پیام متناسبی را     
     نمایش دهید
    """

    def search_for_stores(self):
        seerch_for = (input("Enter the store name : ")).lower()
        with open("userinfo.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if "manager" == row['username']:
                    if seerch_for == row['store_name']:
                        print(f'there is {row["store_name"]} store! ')
                    else:
                        print(f'Oops! there is not {seerch_for}')

    """
    انتخاب فروشگاه
    
    مشتری می تواند از بین فروشگاه هایی که به وی نمایش داده شده یکی را انتخاب کند
    """

    def choose_for_stores(self):
        with open("userinfo.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if "manager" == row['username']:
                    print(row['store_name'], end='\n')
            choose_one = input("enter one name of stores ")
            with open("userinfo.csv", "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if choose_one == row['store_name']:
                        print("you are lucky to find")
                        break

    """
    مشاهده لیست کالاها
    مشتری بعد از انتخاب فروشگاه مورد نظر خود، می تواند لیست اجناس قابل خرید آن 
فروشگاه را مشاهده نماید.نام، برند و قیمت کاال ها به مشتری نمایش داده می شود.    
    """

    def see_products(self):
        with open("userinfo.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if "manager" == row['username']:
                    print(row['store_name'], end='\n')
        store_name = input("enter one of ")
        with open("userinfo.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if store_name == row['store_name']:
                    self.store_name = row['store_name']
                    self.username = row['username']
                    with open('ShopManager_Info.csv', 'r') as f:
                        reader_shop = csv.DictReader(f)
                        for row_shop in reader_shop:
                            if self.username == row_shop['username']:
                                print(row_shop)
                        choose_prod = int(input("if you want to choose a product enter 1 for exit press other number "))
                        if choose_prod == 1:
                            self.choose_products_and_add()
                        else:
                            break

    """
    
    جستجوی کالا
    مشتری می تواند بر اساس نام و برند اجناس جست و جو کند و مشخصات کاال رو مشاهده 
کرده و در صورت موجود بودن به لیست خرید اضافه کند.   
    """

    def choose_products_and_add(self):
        self.p_name = input("brand name : ")
        with open("ShopManager_Info.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if self.p_name == row['p_name']:
                    print(row['p_name'], end='\n')
            if row['p_num_stocks'] > 0:
                with open("factor.csv", 'a') as f:
                    column = ['store_name', 'username', 'p_name', 'p_num_stocks', 'exp_date', 'p_barcode']
                    write = csv.DictWriter(f, fieldnames=column)
                    write.writerows([{'store_name': self.storename, 'username': self.username, 'p_name': self.p_name,
                                      'p_num_stocks':self.p_num_stocks, 'exp_date':self.exp_date, 'p_barcode':self.p_barcode}])
