# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод
команды show cdp neighbor из нескольких файлов и записывает итоговую
топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами,
независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь
в файл topology.yaml. Он понадобится в следующем задании.

"""

from glob import glob
import re
import yaml

def parse_sh_cdp_neighbors(command):
    regexp =r'^(?P<dev>\w+)>' \
            r'|^(?P<dev_neig>\w+) +(?P<intf_loc>\w+ \S+)\s+\d+.*?(?P<port>\w+ \S+)$'
    result = {}

    match = re.finditer(regexp, command, re.DOTALL | re.MULTILINE)
    dev = None

    for m in match:
        if m.group('dev'):
            dev = m.group('dev')
            result[dev] = {}
        else:
            result[dev][m.group('intf_loc')] = {m.group('dev_neig') : m.group('port')}

    return result

def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    topology_dict = {}

    for filename in list_of_files:
        with open(filename) as f:
            command = f.read()
            result = parse_sh_cdp_neighbors(command)
            print(result)
            topology_dict.update(result)

    if save_to_filename:
        with open(save_to_filename, 'w') as file:
            yaml.dump(topology_dict, file)

    return topology_dict

if __name__ == '__main__':
    files = glob("sh_cdp_n_*")
    topology_dict = generate_topology_from_cdp(files, 'topology.yaml')
    print(topology_dict)
