from etl import *

fluxoHuawei.display_station_all()

lista_mac = gerar_lista_mac(WorldItem.lista_stations)

dispositivo = {
    'device_type': 'huawei',
    'host': '172.17.1.150',
    'username': os.getenv('USUARIO'),
    'password': os.getenv('PASSWORD'),
    'global_delay_factor': 0.1,
}

connection = ConnectHandler(**dispositivo)
connection.enable()

command = 'display station statistics sta-mac '

stations_statistics = []

for mac in lista_mac:
    # criar função para output

    output = connection.send_command(command + mac)

    output = output.replace(output[0:78], mac, 1)
    output = output.replace(output[-80:], '', 1)
    output = output.replace('Packets sent to the station', '')
    output = output.replace('Packets received from the station', '')
    output = output.replace('Bytes sent to the station', '')
    output = output.replace('Bytes received from the station', '')
    output = output.replace('Wireless data rate sent to the station(kbps)', '')
    output = output.replace('Wireless data rate received from the station(kbps)', '')
    output = output.replace('Trigger roam total', '')
    output = output.replace('Trigger roam failed', '')
    output = output.replace('STA power save percent', '')
    output = output.replace(':', '')
    output = output.replace(' ', '')
    output = output.split('\n')

    stations_statistics.append(output)

    print(stations_statistics)

connection.disconnect()

# %%

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def teste():
    asyncio.run(steps())


set_interval(teste, 30)
##
#!/usr/bin/python3
from elasticsearch import Elasticsearch, helpers
from pkg_rsrcs import (
    asyncio, time,
    csv, os
)
import pandas as pd
from utils import (
    gerar_lista_mac,
    fluxoHuawei,
    WorldItem,
)

stepIn = fluxoHuawei()


async def first_step():
    await asyncio.sleep(0.5)
    print(f'Iniciando step 1: {time.strftime("%H:%M:%S")}')
    stepIn.get_users_stations()


async def second_step():
    await asyncio.sleep(0.5)
    print(f'Iniciando step 2: {time.strftime("%H:%M:%S")}')


async def third_step():
    await asyncio.sleep(0.5)
    print(f'Iniciando step 3: {time.strftime("%H:%M:%S")}')


async def fourth_step():
    await asyncio.sleep(0.5)


async def fifth_step():
    await asyncio.sleep(0.5)


async def steps():
    print(f'Iniciando o fluxo de steps {time.strftime("%H:%M:%S")}')

    first_task = asyncio.create_task(first_step())
    await first_task
    second_task = asyncio.create_task(second_step())
    await second_task
    third_task = asyncio.create_task(third_step())
    await third_task
    fourth_task = asyncio.create_task(fourth_step())
    await fourth_task
    fifth_task = asyncio.create_task(fifth_step())
    await fifth_task

    print(f'Finalizando o fluxo de steps {time.strftime("%H:%M:%S")}')

asyncio.run(steps())
