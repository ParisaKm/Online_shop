import file_Handler
from file_Handler import ShopManager


while True:
    customer_manager = int(input("customer=>1 or manager=>2 : "))
    if customer_manager == 1:
        n = int(input("for sign up enter 1 / for sign in enter 2 : "))
        if n == 1:
            file_Handler.sign_up()
            break
        elif n == 2:
            file_Handler.sign_in()
            break
        else:
            break
    elif customer_manager == 2:
        n = int(input("for sign up as manager enter 1 / for sign in as manager enter 2 : "))
        if n == 1:
            ShopManager.sign_up()
            break
        elif n == 2:
            ShopManager.sign_in()
            break
        else:
            break
