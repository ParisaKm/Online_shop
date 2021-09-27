import file_Handler
from file_Handler import ShopManager
from file_Handler import Customer
from file_Handler import ShopManagerMenu


def main_menu():

    while True:
        customer_manager = int(input("customer=>1 or manager=>2 : "))
        if customer_manager == 1:
            n = int(input("for sign up enter 1 / for sign in enter 2 : "))
            if n == 1:
                Customer.sign_up()
                break
            elif n == 2:
                Customer.sign_in()
            else:
                break
        elif customer_manager == 2:
            n = int(input("for sign up as manager enter 1 / for sign in as manager enter 2 : "))
            if n == 1:
                ShopManager.sign_up()
                break
            elif n == 2:
                signed = ShopManager.sign_in()
                if signed:
                    ShopManagerMenu.alert_of_ending_stocks()

                else:
                    print("Something was wrong! try again")
                    continue
            else:
                break


# ShopManagerMenu.alert_of_ending_stocks()
print(main_menu())