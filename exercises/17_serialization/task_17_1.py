# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла, c
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""

import re
import csv

def write_dhcp_snooping_to_csv(files, output):
    result_file = open(output, 'w', newline='', encoding='utf-8')
    writer = csv.writer(result_file)
    headers = ['switch','mac','ip','vlan','interface']
    writer.writerow(headers)

    for file in files:
        with open(file) as f:
            match = re.search(r'(\w+?)_.+', file)
            if match:
                switch = match.group(1)
            else:
                switch = None

            lines = f.read()
            # 00:09:BB:3D:D6:58   10.1.10.2        86250       dhcp-snooping   10    FastEthernet0/1
            data = re.finditer(r'^(?P<mac>\d.+?)\s+(?P<ip>\S+).*?(?P<vlan>\d+)\s+(?P<intf>\w+/\d+)$', lines, re.MULTILINE)
            for d in data:
                row = [switch, d['mac'], d['ip'], d['vlan'], d['intf']]
                writer.writerow(row)

    result_file.close()
    return None

if __name__ == '__main__':
    files = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
    write_dhcp_snooping_to_csv(files, 'output.csv')