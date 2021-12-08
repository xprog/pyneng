# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_is_correct = False

while ip_is_correct == False:
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

    if ip_is_correct == False:
        print("Неправильный IP-адрес")

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
