# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import re
from pprint import pprint

def parse_sh_ip_int_br(filename):
    regex = r'(\S+) +(\S+) +(?:\w+) +(?:\w+) +(administratively down|up|down) +(up|down)'
    result = []

    with open(filename) as lines:
        for line in lines:
            m = re.search(regex, line, re.MULTILINE)
            if m:
                result.append(m.groups())

    return result

if __name__ == "__main__":
    result = parse_sh_ip_int_br("sh_ip_int_br.txt")
    pprint(result)
