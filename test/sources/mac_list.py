from lista_stations import lista_stations
from utils import gerar_lista_mac

lista_mac = gerar_lista_mac(lista_stations)

mac_list = lista_mac

# async def task_1():
#     exec(open("utils.py").read())
#
#
# async def task_2():
#     exec(open("etl.py").read())
#
#
# async def task_3():
#     exec(open("actions.py").read())
#
#
# async def executar_scripts():
#     print(f'Iniciando scripts {time.strftime("%H:%M:%S")}')
#     scrip1 = asyncio.create_task(task_1())
#     script2 = asyncio.create_task(task_2())
#     # script3 = asyncio.create_task(task_3())
#     await scrip1
#     await script2
#     # await script3
#     print(f'Finalizando scripts {time.strftime("%H:%M:%S")}')
#
#
# asyncio.run(executar_scripts())
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
    stepIn.display_access_users()


async def second_step():
    await asyncio.sleep(0.5)
    print(f'Iniciando step 2: {time.strftime("%H:%M:%S")}')
    stepIn.display_station_all()


async def third_step():
    await asyncio.sleep(0.5)
    print(f'Iniciando step 3: {time.strftime("%H:%M:%S")}')
    gerar_lista_mac(WorldItem.lista_stations)
    WorldItem.lista_mac = gerar_lista_mac(
        WorldItem.lista_stations
    )
    return WorldItem.lista_mac


async def fourth_step():
    await asyncio.sleep(0.5)
    print(f'Iniciando step 4: {time.strftime("%H:%M:%S")}')
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
    print(f'Iniciando step 5: {time.strftime("%H:%M:%S")}')
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
    await first_task
    second_task = asyncio.create_task(second_step())
    await second_task
    # third_task = asyncio.create_task(third_step())
    # await third_task
    # fourth_task = asyncio.create_task(fourth_step())
    # await fourth_task
    # fifth_task = asyncio.create_task(fifth_step())
    # await fifth_task

    print(f'Finalizando o fluxo de steps {time.strftime("%H:%M:%S")}')

asyncio.run(steps())
