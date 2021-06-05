from curses.ascii import isdigit
from random import randint

"""
get numbers form user

"""


def get_value():
    value = input("podaj liczbę z zakresu 1-49 : ")
    try:
        value = int(value)
        return value
    except ValueError:
        print("niepoprawna wartość")
    except TypeError:
        print("niepoprawna wartość")


"""
check if value is a number 
check if   number in range 1- 49
 """


def value_check(val):
    try:
        # if isdigit(val) and val != "/":
        if val in range(1, 50):
            return val
        else:
            print("liczba z poza zakresu")
    except ValueError:
        print("niepoprawna wartość")
    except TypeError:
        print("niepoprawna wartość")


"""
add to list 
"""


def user_nums():
    user_num_list = []
    while len(user_num_list) < 6:
        val = value_check(get_value())
        if val not in user_num_list and val !=None:
            user_num_list.append(val)
        return user_num_list


"""
draw numbers
"""


def drawing_machine():
    ball = 0
    balls = []
    while len(balls) < 6:
        if ball not in balls and ball > 0:
            balls.append(ball)
        else:
            ball = randint(1, 49)
    return balls


""""
sorting lists of numbers
"""


def sorter(num_lis):
    sorted_num_lis = sorted(num_lis)
    return sorted_num_lis


"""
compare drawn numbers whit user numbers
"""


def comparison(d_value, user_value):
    win_list = []
    checked_list = user_value
    for value in checked_list:
        if value in d_value:
            win_list.append(value)
    return win_list


"""
show result on the screen

"""


def show_r(w_list):
    if len(w_list) < 6 and len(w_list) != 0:
        print(f"trafiłeś {len(w_list)} liczby oto one :{w_list}")
    elif len(w_list) == 0:
        print(" Pech 0 trafień")
    else:
        print("GRATULACJE!!!!!!!!!!!!!!!!!!!!!!!!  \n  Wygrałeś")


"""
compering all data and show result
"""


def play():
    user_numbers = sorter(user_nums())
    draw_numers = sorter(drawing_machine())
    print(f"twoje liczby : {user_numbers}")
    print(f"wylosowane liczby to: {draw_numers}")
    win_list = comparison(draw_numers, user_numbers)
    show_r(win_list)


play()
