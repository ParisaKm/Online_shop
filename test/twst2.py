class Paris:

    @classmethod
    def name_name(cls, name):
        # name = input("name : ")
        return cls(name=name)

    def __str__(cls):
        print(f'Hi{cls.name}')


Paris.name_name()


# list = []
# for i in range(0,3):
#     x = input("input : ")
#     if x not in list:
#         list.append(x)
#
# print(list)
