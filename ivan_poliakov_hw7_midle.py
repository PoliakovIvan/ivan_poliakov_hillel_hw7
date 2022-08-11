"""TASK 1"""
side_square = float(input('print side of a square \n'))
def square(side):
    print('периметр квадрата: ',side * 4)
    print('диагональ квадрата:', side * 2 ** (0.5))
    print('площадь квадрата:', side * side)
    return side
square(side_square)


"""TASK 2"""
n_month = int(input('Номер місяця: \n'))
def month(number):
    if number > 0 and number < 3:
        print('Зима')
    elif number > 2 and number < 6:
        print('Весна')
    elif number > 5 and number < 9:
        print('Літо')
    elif number > 8 and number < 12:
        print('Осінь')
    elif number == 12:
        print('Зима')
    else:
        print('Будь ласка введіть числа 1-12')
month(n_month)

"""TASK 3"""

list1: list = [1, 2, 3]
list2: list = [11, 22, 33]
list3: list = []
def gen(l1, l2, l3):
    for i in l1:
        l3.append(i)

        for j in l2:
            l3.append(j)
            l2.remove(j)
            break
    print(list3)
gen(list1, list2, list3)


"""TASK 4"""
pl = input('print something \n')
pl1 = ''
pl2 = ''
def polindrom():
    pl1 = pl[:len(pl)//2]
    pl2 = pl[len(pl)//2:]
    pl2 = pl2[::-1]
    if pl1 == pl2:
        print(True)
    else:
        print(False)
polindrom()
