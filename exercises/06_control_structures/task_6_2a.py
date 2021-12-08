# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input("введите IP-адрес в формате 10.0.1.1: ")
ips = ip.split(".")

ip_is_correct = True

# проверка введенного IP-адреса
if ip.count(".") == 3 and len(ips) == 4:
    for ip_oct in ips:
        if ip_oct.isdigit() and int(ip_oct) >= 0 and int(ip_oct) <= 255:
            pass
        else:
            ip_is_correct = False
else:
    ip_is_correct = False


if ip_is_correct == True:
    if int(ips[0]) >= 1 and int(ips[0]) <= 223:
        print('unicast')
    elif int(ips[0]) >= 224 and int(ips[0]) <= 239:
        print('multicast')
    elif ip == "255.255.255.255":
        print('local broadcast')
    elif ip == "0.0.0.0":
        print('unassigned')
    else:
        print('unused')
else:
    print("Неправильный IP-адрес")