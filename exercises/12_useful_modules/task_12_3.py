# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

from tabulate import tabulate

def print_ip_table(list_reachable, list_unreachable):
    ip_dict = {}
    ip_dict['Reachable'] = list_reachable
    ip_dict['Unreachable'] = list_unreachable

    print(tabulate(ip_dict, headers='keys'))

if __name__ == '__main__':
    list_reachable = ['192.168.1.190', '192.168.1.191', '192.168.1.192', '192.168.1.193', '192.168.1.194', '192.168.1.195']
    list_unreachable = ['10.3.1.10', '10.3.1.11', '10.3.1.12', '10.3.1.13']
    print_ip_table(list_reachable, list_unreachable)