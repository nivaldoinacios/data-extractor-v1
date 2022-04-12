#!/usr/bin/python3
import pandas as pd
from pkg_rsrcs import (asyncio, time, os)
from utils import (gerar_lista_mac, fluxoHuawei, WorldItem)


async def first_step():
    e = 'Step 1'
    print(f'Iniciando {e}: {time.strftime("%H:%M:%S")}')

    try:
        fluxoHuawei.get_users_stations()
    except Exception as e:
        print(f'Erro ao executar o : {e}')

    print(f'{e} Concluido: {time.strftime("%H:%M:%S")}')

    return WorldItem.list_users, WorldItem.list_stations



async def second_step():
    e = 'Step 2'
    print(f'Iniciando {e}: {time.strftime("%H:%M:%S")}')

    gerar_lista_mac(WorldItem.list_stations)
    WorldItem.list_mac = gerar_lista_mac(
        WorldItem.list_stations
    )

    print(f'{e} Concluido: {time.strftime("%H:%M:%S")}')

    return WorldItem.list_mac


async def third_step():
    e = 'Step 3'
    print(f'Iniciando {e}: {time.strftime("%H:%M:%S")}')

    df_stations_all = pd.DataFrame(WorldItem.list_stations,
                                   columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
                                            'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID',
                                            "@timestamp-py"])

    df_access_users = pd.DataFrame(WorldItem.list_users, columns=["UserID", "Username", "IPADDRESS", "MAC",
                                                                  "Status", "@timestamp-py"])

    WorldItem.df = pd.merge(df_access_users, df_stations_all, how='outer', on=['MAC'])
    WorldItem.df = WorldItem.df.drop(columns=['IPADDRESS_y', '@timestamp-py_x'])
    WorldItem.df = WorldItem.df.rename(columns={'@timestamp-py_y': '@timestamp-py'})
    WorldItem.df = WorldItem.df.rename(columns={'IPADDRESS_x': 'IPADDRESS'})
    WorldItem.df = WorldItem.df.fillna(0)

    WorldItem.df.to_csv(path_or_buf=os.getenv('dir_users_stations'), sep=';',
                        columns=['UserID', 'Username', 'IPADDRESS', 'MAC', 'Status', 'AP_ID',
                                 'AP_NAME', 'RF/WLAN', 'BAND', 'Type', 'RX/TX', 'RSSI', 'VLAN',
                                 'SSID', '@timestamp-py'],
                        header=True, index=True, index_label='index', line_terminator='\n')

    print(f'{e} Concluido: {time.strftime("%H:%M:%S")}')

    return WorldItem.df


# async def fourth_step():
#     await asyncio.sleep(0.5)
#
#
# async def fifth_step():
#     await asyncio.sleep(0.5)


async def main():
    print(f'Iniciando o fluxo de steps {time.strftime("%H:%M:%S")}')

    await first_step()
    await second_step()
    await third_step()
    # await fourth_task
    # await fifth_task
    print(f'Finalizando o fluxo de steps {time.strftime("%H:%M:%S")}')


asyncio.run(main())
