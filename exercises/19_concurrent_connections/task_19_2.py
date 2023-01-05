# -*- coding: utf-8 -*-
"""
Задание 19.2

Создать функцию send_show_command_to_devices, которая отправляет одну и ту же
команду show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя текстового файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в обычный текстовый файл в таком формате
(перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
"""
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
import netmiko
import yaml
import re
import logging

def send_show_command_to_device(device, command):
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            result = ssh.send_command(command, strip_prompt=False, strip_command=False)
            return result
    except netmiko.NetmikoTimeoutException as error:
        print(f'Не удалось подключиться к {device["host"]}')
    except netmiko.NetmikoAuthenticationException as error:
        print(f'Ошибка аутентификации с {device["host"]}')


def send_show_command_to_devices(devices, command, filename, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(send_show_command_to_device, devices, repeat(command))
        with open(filename, 'w') as file_result:
            for res in result:
                output = result_modify(res)
                file_result.write(output)


def result_modify(input):
    hostname = re.search('(\S+)>$', input).group(1)
    data = re.search('(.+)\n\S+>$', input, re.DOTALL).group(1)
    output = re.sub('(.+)\n(\S+)>$', r'\2#\1', input, re.DOTALL)
    print(input)
    print('x'*60)
    print(data)
    print('-'*30)
    output = f'{hostname}#{data}'
    print(output)
    print('+'*30)
    # print(hostname)
    # output = hostname
    return output


if __name__ == '__main__':
    with open('devices.yaml') as file:
        devices = yaml.safe_load(file)

        # result = send_show_command_to_device(devices[0], 'show ip int br')
        # print(result)

        send_show_command_to_devices(devices, 'show ip int br', 'file_result.txt')