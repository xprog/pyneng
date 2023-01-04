# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""

import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor

def ping_ip_address(ip):
    if platform.system().lower() == 'windows':
        cmd = 'ping -n 2 {}'
    else:
        cmd = 'ping -c 2 {}'
    process = subprocess.run(cmd.format(ip).split(),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             encoding='utf-8')
    if process.returncode == 0 and 'unreachable' not in process.stdout:
        return True, process.stdout
    else:
        return False, process.stdout + process.stderr


def ping_ip_addresses(ip_list, limit=3):
    list_ip_reachable = []
    list_ip_unreachable = []

    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(ping_ip_address, ip_list)

        for ip, output in zip(ip_list, result):
            # print(ip, output)
            if output[0]:
                list_ip_reachable.append(ip)
            else:
                list_ip_unreachable.append(ip)

    return list_ip_reachable, list_ip_unreachable

if __name__ == '__main__':
    ip = '192.168.1.190'
    result, output = ping_ip_address(ip)
    print(result, output)

    ip_list = ['192.168.1.190', '192.168.1.199', '8.8.8.8']
    list_ip_online, list_ip_offline = ping_ip_addresses(ip_list)
    print(list_ip_online)
    print(list_ip_offline)
