from pkg_resources import asyncio, time, os
import pandas as pd
from utils import (
    gerar_lista_mac,
    fluxoHuawei,
    WorldItem,
)

stepIn = fluxoHuawei()


async def first_step():
    await asyncio.sleep(1)
    stepIn.display_access_users()


async def second_step():
    await asyncio.sleep(1)
    stepIn.display_station_all()


async def third_step():
    await asyncio.sleep(1)
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


async def steps():
    print(f'Iniciando o fluxo de steps {time.strftime("%H:%M:%S")}')

    first_task = asyncio.create_task(first_step())
    second_task = asyncio.create_task(second_step())
    third_task = asyncio.create_task(third_step())
    fourth_task = asyncio.create_task(fourth_step())
    await first_task
    await second_task
    await third_task
    await fourth_task
    print(f'Finalizando o fluxo de steps {time.strftime("%H:%M:%S")}')


asyncio.run(steps())
