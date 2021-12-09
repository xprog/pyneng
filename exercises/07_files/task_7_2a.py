# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

ignore = ["duplex", "alias", "configuration"]

is_ignore_string = False

with open(argv[1]) as f:
    line = True

    while line:
        is_ignore_string = False
        line = f.readline()
        if not line.strip().startswith("!"):
            for ign in ignore:
                if ign in line:
                    is_ignore_string = True

            if is_ignore_string == False:
                print(line.strip("\n"))