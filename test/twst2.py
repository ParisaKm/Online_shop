# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def __str__(self):
#         print(f'name : {self.name}, max_speed : {self.max_speed}, mileage : {self.mileage}')
#
#
# class Bus(Vehicle):
#     pass

# Bus('School volvo', 120, 12).__str__()
"""----------------------------------------------------------"""

class Sa:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def inputing(self):
        self.user = input(" user ")
        self.password = input(" password ")
        return f'{self.user} {self.password}'

obj = Sa('user','password')
obj.inputing()
"""----------------------------------------------------------"""
# class Paris:
#
#     @classmethod
#     def name_name(cls, name):
#         # name = input("name : ")
#         return cls(name=name)
#
#     def __str__(cls):
#         print(f'Hi{cls.name}')


# Paris.name_name()


# list = []
# for i in range(0,3):
#     x = input("input : ")
#     if x not in list:
#         list.append(x)
#
# print(list)
