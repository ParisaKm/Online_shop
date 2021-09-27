import tkinter
from tkinter import messagebox

# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()
a = 'Parisa'
# Message Box
messagebox.showinfo(a, "Message")

# import warnings
# import logging
#
# #
# #
# # class WarnExample:
# #     def __init__(self):
# #         self.text = "Warning"
# #
# #
# #     def method1(self):
# #         warnings.warn("method1 is deprecated, use new_method instead",DeprecationWarning)
# #         print('method1', len(self.text))
# #
# #     def method2(self):
# #         warnings.warn(
# #             "method2 will be deprecated in version 2, use new_method instead",
# #             PendingDeprecationWarning
# #         )
# #         print('method2', len(self.text))
# #
# #     def new_method(self):
# #         print('new method', len(self.text))
# #
# #
# # if __name__ == '__main__':
# #     e = WarnExample()
# #     e.method1()
# #     e.method2()
# #     e.new_method()
# def is_zero(i):
#     if i != 0:
#         print("OK")
#     else:
#         logger = logging.getLogger("Manager related")
#         logging.basicConfig(level=logging.DEBUG,
#                             filename='app.log',
#                             format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s' \n",
#                             datefmt='%d-%b-%y %H:%M:%S')
#         # warnings.warn("the input is 0!")
#     return i
#
#
# is_zero(0)
#
# import re
# import csv
# import hashlib
#
# #
# #
# #
# # for i in range(2):
# #     username = input("enter phone_num as username : ")
# #     x = re.findall("09\d{9}", username)
# #     if [username] != x:
# #         print("Wrong number!")
# #
# #     elif [username] == x:
# #         with open("test.csv", "r") as csvfile:
# #             reader = csv.DictReader(csvfile)
# #             for row in reader:
# #                 if username != row["username"]:
# #                     break
# #             print("you were applied!")
# #     else:
# #         break
# #
# # password = input("enter password: ")
# # Password = hashlib.sha256(password.encode('utf-8')).hexdigest()
# # with open('test.csv', 'a') as csvfile:
# #     columns = ['username', 'password']
# #     writer = csv.DictWriter(csvfile, fieldnames=columns)
# #     if csvfile.tell() == 0:
# #         writer.writeheader()
# #     writer.writerows([{'username': username, 'password': Password}])
# #     print("you signed in successfully")
