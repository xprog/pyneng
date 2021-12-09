# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]

is_ignore_string = False

with open(argv[1]) as f_src, open(argv[2], "w") as f_dst:
    line = True

    while line:
        is_ignore_string = False
        line = f_src.readline()
        if not line.strip().startswith("!"):
            for ign in ignore:
                if ign in line:
                    is_ignore_string = True

            if is_ignore_string == False:
                f_dst.write(line)