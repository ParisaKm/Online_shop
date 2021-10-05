from person import Person
from file_Handler import Customer

def main_menu():
    signup_signin = int(input("sign up=>1 , sign in=>2 or exit =any number: "))
    while signup_signin != 3:
        if signup_signin == 1:
            Person.sign_up()
            a = int(input("if you want to sign in press 1 if not other number"))
            if a == 1:
                p = Person()
                p.sign_in()
            else:
                break
        elif signup_signin == 2:
            p = Person()
            p.sign_in()
            break
        else:
            print("see you soon bye")
            break

c = Customer('user','pass','post')
p = Person()
# p.sign_in('user','pass')
# print(main_menu())
c.see_products()