# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

template = """
Prefix              {}
AD/Metric           {}
Next-Hop            {}
Last update         {}
Outbound Interface  {}"""

with open("ospf.txt") as f:
    data = f.readlines()
    for line in data:
        _, prefix, metric, _, next_hop, last_update, out_intf = line.strip().split()
        # print(line.strip().split())
        print(template.format(prefix, metric.strip("[]"), next_hop.strip(","), last_update.strip(","), out_intf))