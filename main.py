# import access_user
from ListaMac import mac_list
# import stations
# import neighbor

mac_list = str(mac_list)
print(mac_list.split('\n'))
for mac in mac_list.split('\n'):
    print(mac[-14::])
#%%