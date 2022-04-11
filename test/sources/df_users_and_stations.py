# from lista_stations import lista_stations
# from lista_users import lista_users
# import pandas as pd
#
# df_stations = pd.DataFrame(lista_stations, columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
#                                                     'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID', "@timestamp-py"])
#
# df_users = pd.DataFrame(lista_users, columns=["UserID", "Username", "IPADDRESS", "MAC",
#                                               "Status", "@timestamp-py"])
#
# df = pd.merge(df_users, df_stations, how='outer', on=['MAC'])
# df = df.drop(columns=['IPADDRESS_y', '@timestamp-py_x'])
# df = df.rename(columns={'@timestamp-py_y': '@timestamp-py'})
# df = df.rename(columns={'IPADDRESS_x': 'IPADDRESS'})
#
# df = df.fillna(0)
#
# df
#
#
#
# # #%%
# # import pandas as pd
# #
# # from pkg_resources import WorldItem
# #
# # df_stations = pd.DataFrame(WorldItem.lista_stations, columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
# #                                                               'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID',
# #                                                               "@timestamp-py"])
# #
# # df_users = pd.DataFrame(WorldItem.lista_users, columns=["UserID", "Username", "IPADDRESS", "MAC",
# #                                                         "Status", "@timestamp-py"])
# #
# # df = pd.merge(df_users, df_stations, how='outer', on=['MAC'])
# # # df = df.drop(columns=['IPADDRESS_y', '@timestamp-py_x'])
# # # df = df.rename(columns={'@timestamp-py_y': '@timestamp-py'})
# # # df = df.rename(columns={'IPADDRESS_x': 'IPADDRESS'})
# # #
# # # df = df.fillna(0)
# #
# # #%%
# # df_users
# # #%%
# ########$$$$$$$$$$$
# #
# # es = Elasticsearch(
# #     ['http://192.168.10.14:9200'],
# #     basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
# # )
# #
# # df_ed = ed.pandas_to_eland(
# #     pd_df=df,
# #     es_client=es,
# #     es_dest_index='eland-fluxo',
# #     es_type_overrides={
# #         "@timestamp": "date"
# #     },
# #     es_if_exists='append',
# #     es_refresh=True,
# # )
# #
# # exec('df_ed')
# #
# # time.sleep(2)
# #
# # df.to_csv(os.getenv('dir_users_stations'), sep=';', na_rep=0, header=False, index=False, line_terminator='\n')
#
# ###
# # df.to_csv(os.getenv('dir_users_stations'), sep=';', header=True, index=False, line_terminator='\n')
# # i = df.to_csv(path_or_buf=None, sep=';', na_rep=0, header=False, index=False, line_terminator='\n')
# # i.split('\n').pop()
# # ed.csv_to_eland(
# #     filepath_or_buffer=textStream,
# #     es_client=es,
# #     es_dest_index='teste',
# #     es_if_exists='replace',
# #     es_refresh=True,
# # )
#
# ###################
# es = Elasticsearch(
#     ['http://192.168.10.14:9200'],
#     basic_auth=(os.getenv('ELK_USERNAME'), os.getenv('ELK_PASSWORD'))
# )
# #%%
# textStream = StringIO(newline='\n')
# #%%
# df.to_csv(path_or_buf=textStream, sep=';', columns=['UserID', 'Username', 'IPADDRESS', 'MAC', 'Status', 'AP_ID',
#                                                     'AP_NAME', 'RF/WLAN', 'BAND', 'Type', 'RX/TX', 'RSSI', 'VLAN',
#                                                     'SSID', '@timestamp-py'],
#           header=True, index=True, index_label='index', line_terminator='\n')
# #%%
# print(textStream.getvalue())
# #%%
# ed.csv_to_eland(
#     filepath_or_buffer=textStream,
#     es_client=es,
#     es_dest_index='teste',
#     es_if_exists='replace',
#     es_refresh=True,
# )
# #%%
# print(textStream.getvalue())
# #%%
# time.sleep(0.2)
#
# df_stations_all = pd.DataFrame(WorldItem.lista_stations, columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
#                                                                   'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID',
#                                                                   "@timestamp-py"])
#
# df_access_users = pd.DataFrame(WorldItem.lista_users, columns=["UserID", "Username", "IPADDRESS", "MAC",
#                                                                "Status", "@timestamp-py"])
#
# df = pd.merge(df_access_users, df_stations_all, how='outer', on=['MAC'])
# df = df.drop(columns=['IPADDRESS_y', '@timestamp-py_x'])
# df = df.rename(columns={'@timestamp-py_y': '@timestamp-py'})
# df = df.rename(columns={'IPADDRESS_x': 'IPADDRESS'})
# df = df.fillna(0)
#
# df.to_csv(path_or_buf=os.getenv('dir_users_stations'), sep=';',
#           columns=['UserID', 'Username', 'IPADDRESS', 'MAC', 'Status', 'AP_ID',
#                    'AP_NAME', 'RF/WLAN', 'BAND', 'Type', 'RX/TX', 'RSSI', 'VLAN',
#                    'SSID', '@timestamp-py'],
#           header=True, index=True, index_label='index', line_terminator='\n')
# ############
# # import etl
# #
# # df_stations_all = pd.DataFrame(WorldItem.lista_stations, columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND',
# # 'Type', 'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID', "@timestamp-py"])
# #
# # df_access_users = pd.DataFrame(WorldItem.lista_users, columns=["UserID", "Username", "IPADDRESS", "MAC",
# #                                                                "Status", "@timestamp-py"])
# #
# # df = pd.merge(df_access_users, df_stations_all, how='outer', on=['MAC'])
# # df = df.drop(columns=['IPADDRESS_y', '@timestamp-py_x'])
# # df = df.rename(columns={'@timestamp-py_y': '@timestamp-py'})
# # df = df.rename(columns={'IPADDRESS_x': 'IPADDRESS'})
# # df = df.fillna(0)
# #
# # df.to_csv(path_or_buf=os.getenv('dir_users_stations'), sep=';',
# #           columns=['UserID', 'Username', 'IPADDRESS', 'MAC', 'Status', 'AP_ID',
# #                    'AP_NAME', 'RF/WLAN', 'BAND', 'Type', 'RX/TX', 'RSSI', 'VLAN',
# #                    'SSID', '@timestamp-py'],
# #           header=True, index=True, index_label='index', line_terminator='\n')
#
# # time.sleep(0.2)
# #
# # df_stations_all = pd.DataFrame(WorldItem.lista_stations, columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
# #                                                                   'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID',
# #                                                                   "@timestamp-py"])
# #
# # df_access_users = pd.DataFrame(WorldItem.lista_users, columns=["UserID", "Username", "IPADDRESS", "MAC",
# #                                                                "Status", "@timestamp-py"])
# #
# #
# # df = pd.merge(df_access_users, df_stations_all, how='outer', on=['MAC'])
# # df = df.drop(columns=['IPADDRESS_y', '@timestamp-py_x'])
# # df = df.rename(columns={'@timestamp-py_y': '@timestamp-py'})
# # df = df.rename(columns={'IPADDRESS_x': 'IPADDRESS'})
# # df = df.fillna(0)
# #
# # df.to_csv(path_or_buf=os.getenv('dir_users_stations'), sep=';',
# #           columns=['UserID', 'Username', 'IPADDRESS', 'MAC', 'Status', 'AP_ID',
# #                    'AP_NAME', 'RF/WLAN', 'BAND', 'Type', 'RX/TX', 'RSSI', 'VLAN',
# #                    'SSID', '@timestamp-py'],
# #           header=True, index=True, index_label='index', line_terminator='\n')
# df_stations_all = pd.DataFrame(WorldItem.lista_stations,
#                                columns=['MAC', 'AP_ID', 'AP_NAME', 'RF/WLAN', 'BAND', 'Type',
#                                         'RX/TX', 'RSSI', 'VLAN', 'IPADDRESS', 'SSID',
#                                         "@timestamp-py"])
#
# df_access_users = pd.DataFrame(WorldItem.lista_users, columns=["UserID", "Username", "IPADDRESS", "MAC",
#                                                                "Status", "@timestamp-py"])
#
# df = pd.merge(df_access_users, df_stations_all, how='outer', on=['MAC'])
# df = df.drop(columns=['IPADDRESS_y', '@timestamp-py_x'])
# df = df.rename(columns={'@timestamp-py_y': '@timestamp-py'})
# df = df.rename(columns={'IPADDRESS_x': 'IPADDRESS'})
# df = df.fillna(0)
