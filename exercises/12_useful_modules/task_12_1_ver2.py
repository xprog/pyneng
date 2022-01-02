# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess


def ping_ip_addresses(ip_list):
    ip_online = []
    ip_offline = []
    processes = []

    for ip in ip_list:
        p = subprocess.Popen(f'ping -n 2 -w 500 {ip}'.split(' '),
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                encoding='UTF-8')
        processes.append(p)

    for ip, process in zip(ip_list, processes):
        returncode = process.wait()
        if returncode == 0:
            ip_online.append(ip)
        else:
            ip_offline.append(ip)

    return ip_online, ip_offline



if __name__ == '__main__':
    ip_list = ['192.168.1.190', '10.3.1.10', '10.10.10.10']
    ip_online, ip_offline = ping_ip_addresses(ip_list)
    print(ip_online, ip_offline)