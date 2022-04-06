from utils import (limpar_output, separar_campos)
from display_station_all import output

regx = '^([0-9A-Fa-f]{4}[:-])'

# limpar_output(output, regx)

lista_stations = limpar_output(output, regx)

# separar_campos(lista_stations)

lista_stations = separar_campos(lista_stations)


def __init__(self):
    self.net_connect = ConnectHandler(**homeRTR)


def show_dhcp_binding(self, mac_end):
    command = 'show ip dhcp binding | incl ' + mac_end
    output = self.net_connect.send_command(command)
    #        self.net_connect.disconnect()
    return output.split('\n')


def ping_ipaddr(self, ipaddr):
    command = 'ping ' + ipaddr
    output = self.net_connect.send_command(command)
    #        self.net_connect.disconnect()
    return output.split('\n')


def show_arp(self, mac_end):
    command = 'show arp | incl ' + mac_end
    output = self.net_connect.send_command(command)
    #        self.net_connect.disconnect()
    return output.split('\n')


def add_dhcp_client(self, config_list):
    output = self.net_connect.send_config_set(config_list)
    return output.split('\n')


def delete_dhcp_client(self, config_list):
    output = self.net_connect.send_config_set(config_list)
    return output.split('\n')
