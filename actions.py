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
