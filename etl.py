#!/usr/bin/python3
import pandas as pd
from pkg_rsrcs import (time, csv, os)
from elasticsearch import Elasticsearch, helpers
from utils import (gerar_lista_mac, fluxoHuawei, WorldItem)

es = Elasticsearch(
    ['http://192.168.10.14:9200'],
    basic_auth=(
        os.getenv('ELK_USERNAME'),
        os.getenv('ELK_PASSWORD'))
)


def first_step():
    e = 'Step 1'
    print(f'Iniciando {e}: {time.strftime("%H:%M:%S")}')

    try:
        fluxoHuawei.get_users_stations()
    except Exception as e:
        print(f'Erro ao executar o : {e}')

    print(f'{e} Concluido: {time.strftime("%H:%M:%S")}')

    return WorldItem.list_users, WorldItem.list_stations


def second_step():
    e = 'Step 2'
    print(f'Iniciando {e}: {time.strftime("%H:%M:%S")}')

    gerar_lista_mac(WorldItem.list_stations)
    WorldItem.list_mac = gerar_lista_mac(
        WorldItem.list_stations
    )

    print(f'{e} Concluido: {time.strftime("%H:%M:%S")}')

    return WorldItem.list_mac


def third_step():
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


def run():
    print(f'Iniciando o fluxo de steps {time.strftime("%H:%M:%S")}')

    first_step()
    second_step()
    third_step()
    # await fourth_task
    # await fifth_task
    print(f'Finalizando o fluxo de steps {time.strftime("%H:%M:%S")}')


def post_data():
    print(f'Iniciando o post dos dados {time.strftime("%H:%M:%S")}')
    e = 'Post Data'

    try:
        with open(os.getenv('dir_users_stations'), 'r') as f:
            reader = csv.DictReader(f, delimiter=';')
            helpers.bulk(es, reader, index='fluxo')

            time.sleep(1)

            f.close()
    except Exception as e:
        print(f'Erro ao executar o : {e}')

    print(f'Finalizando o post dos dados {time.strftime("%H:%M:%S")}')


run()


post_data()
