# -*- coding: utf-8 -*-
"""
Задание 19.3

Создать функцию send_command_to_devices, которая отправляет разные
команды show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять
  какую команду. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом
команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh int desc
Interface                      Status         Protocol Description
Et0/0                          up             up
Et0/1                          up             up
Et0/2                          admin down     down
Et0/3                          admin down     down
Lo9                            up             up
Lo19                           up             up
R3#sh run | s ^router ospf
router ospf 1
 network 0.0.0.0 255.255.255.255 area 0


Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml и словаре commands
"""

# Этот словарь нужен только для проверки работа кода, в нем можно менять IP-адреса
# тест берет адреса из файла devices.yaml

from concurrent.futures import ThreadPoolExecutor
import netmiko
import yaml
import logging

commands = {
    "192.168.100.3": "sh run | s ^router ospf",
    "192.168.100.1": "sh ip int br",
    "192.168.100.2": "sh int desc",
}

logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)

def send_command_to_device(device, command):
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            result = ssh.send_command(command)
            ssh.enable()
            prompt = ssh.find_prompt()
            return f"{prompt}{command}\n{result}\n"
    except netmiko.NetmikoTimeoutException as error:
        logging.error(f'Не удалось подключиться к {device["host"]}')
    except netmiko.NetmikoAuthenticationException as error:
        logging.error(f'Ошибка аутентификации с {device["host"]}')


def send_command_to_devices(devices, commands_dict, filename, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        with open(filename, 'w') as file_result:
            for device in devices:
                future = executor.submit(send_command_to_device, device, commands_dict[device['host']])
                if future.result():
                    file_result.write(future.result())


if __name__ == '__main__':
    with open('devices.yaml') as file:
        devices = yaml.safe_load(file)
        send_command_to_devices(devices, commands, 'file_result.txt')