# def func(list):                      Функция №1
#     list.insert(0,'start')
#     list.insert(0,'Element')
#     list.append('finish')
#
# list = ['hello', 5, 'John', ]
# func(list)
# print(list)


# def func(list):                   Функция №2
#     a = 0
#     dic ={}
#     for i in list:
#         a = a + 1
#         dic.update({i:a})
#     print(dic)
#
# list = ['x', 5, 'John',]
# dict = func(list)

# def func(b):                        Функция №3
#     list1 = []
#     list2 = []
#     list3 = []
#     list1=list(b)
#     for i in list1:
#         list3.append(i**2)
#         if i % 2 == 0:
#             list2.append(i)
#
#     print(f'Список из кортежа : {list1}')
#     print(f'Список с четными числами : {list2}')
#     print(f'Список с числами в степени 2: {list3}')
#
# b = (1, 2, 3, 4, 5)
# func(b)