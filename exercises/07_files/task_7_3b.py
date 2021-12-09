# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

template = "{:<9}{:20}{}"
result = []

vlan = input("Enter VLAN number: ")

with open("CAM_table.txt") as f:
    data = f.readlines()
    for line in data:
        lines = line.strip().split()
        if len(lines) == 4 and len(lines[1].split(".")) == 3 and lines[0] == vlan:
            result.append(list((int(lines[0]), lines[1], lines[-1])))

result.sort()

for res in result:
    print(template.format(*res))