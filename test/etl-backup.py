from netmiko.huawei import HuaweiTelnet
from pkg_rsrcs import (
    AccessControllers,
    WorldItem,
    re,
)


def limpar_output(output, regx):
    output = output.split('\n')
    result = []

    for line in output:

        if re.search(regx, str(line)) is None:
            pass
        else:
            result.append(line + ' ' + WorldItem.timestamp + '\n')

    return result


def separar_campos(lista):
    result = []

    for line in lista:
        lista = str(lista)

        line = line.strip()

        line = line.split()

        result.append(line)

    return result


def gerar_lista_mac(lista):
    result = []

    for line in lista:
        result.append(line[0])

    return result


# rever o nome do dispositivo e forma de conexao -> 'issue_1'
# criar um metodo para criar um objeto de conexao com o dispositivo


class fluxoHuawei:
    # issue_1
    def __init__(self):
        pass

    @staticmethod
    def display_access_users():

        connection = HuaweiTelnet(**AccessControllers.AC6005,
                                  conn_timeout=60)
        command = 'display access-user'
        output = connection.send_command(command,
                                         read_timeout=60)

        WorldItem.lista_users = limpar_output(
            output,
            WorldItem.regx_userid
        )

        WorldItem.lista_users = separar_campos(
            WorldItem.lista_users
        )

        connection.disconnect()

        return WorldItem.lista_users

    @staticmethod
    def display_station_all():

        connection = HuaweiTelnet(**AccessControllers.AC6005,
                                  conn_timeout=60)
        command = 'display station all'
        output = connection.send_command(command,
                                         read_timeout=60)

        WorldItem.lista_stations = limpar_output(
            output,
            WorldItem.regx_mac
        )

        WorldItem.lista_stations = separar_campos(
            WorldItem.lista_stations
        )

        connection.disconnect()

        return WorldItem.lista_stations

#!/usr/bin/python3
from elasticsearch import Elasticsearch, helpers
from pkg_rsrcs import (
    threading, asyncio,
    time, csv, os
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
    stepIn.display_access_users()


async def second_step():
    await asyncio.sleep(0.5)
    stepIn.display_station_all()


async def third_step():
    await asyncio.sleep(0.5)
    gerar_lista_mac(WorldItem.lista_stations)
    WorldItem.lista_mac = gerar_lista_mac(
        WorldItem.lista_stations
    )
    return WorldItem.lista_mac


async def fourth_step():
    await asyncio.sleep(0.5)
    df_stations_all = pd.DataFrame(WorldItem.lista_stations,
                                   columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
                                            'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID',
                                            "@timestamp-py"])

    df_access_users = pd.DataFrame(WorldItem.lista_users, columns=["UserID", "Username", "IPADDRESS", "MAC",
                                                                   "Status", "@timestamp-py"])

    df = pd.merge(df_access_users, df_stations_all, how='outer', on=['MAC'])
    df = df.drop(columns=['IPADDRESS_y', '@timestamp-py_x'])
    df = df.rename(columns={'@timestamp-py_y': '@timestamp-py'})
    df = df.rename(columns={'IPADDRESS_x': 'IPADDRESS'})
    df = df.fillna(0)

    df.to_csv(path_or_buf=os.getenv('dir_users_stations'), sep=';',
              columns=['UserID', 'Username', 'IPADDRESS', 'MAC', 'Status', 'AP_ID',
                       'AP_NAME', 'RF/WLAN', 'BAND', 'Type', 'RX/TX', 'RSSI', 'VLAN',
                       'SSID', '@timestamp-py'],
              header=True, index=True, index_label='index', line_terminator='\n')
    return df


async def fifth_step():
    await asyncio.sleep(0.5)
    es = Elasticsearch(
        ['http://192.168.10.14:9200'],
        basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
    )

    with open(os.getenv('dir_users_stations'), 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        helpers.bulk(es, reader, index='fluxo')

    f.close()


async def steps():
    print(f'Iniciando o fluxo de steps {time.strftime("%H:%M:%S")}')

    first_task = asyncio.create_task(first_step())
    second_task = asyncio.create_task(second_step())
    third_task = asyncio.create_task(third_step())
    fourth_task = asyncio.create_task(fourth_step())
    fifth_task = asyncio.create_task(fifth_step())
    await first_task
    await second_task
    await third_task
    await fourth_task
    await fifth_task
    print(f'Finalizando o fluxo de steps {time.strftime("%H:%M:%S")}')


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def run():
    asyncio.run(steps())


run()

set_interval(run, 180)
