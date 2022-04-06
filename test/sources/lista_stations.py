from utils import (limpar_output, separar_campos)
from display_station_all import output

regx = '^([0-9A-Fa-f]{4}[:-])'

# limpar_output(output, regx)

lista_stations = limpar_output(output, regx)

# separar_campos(lista_stations)

lista_stations = separar_campos(lista_stations)


stepIn = fluxoHuawei()

stepIn.display_access_users()

stepIn.display_station_all()

lista_mac = gerar_lista_mac(WorldItem.lista_users)

# 1. Gerar lista de MACs
lista_mac = gerar_lista_mac()
# 2. Abrir conexão com o servidor
huawei = HuaweiTelnet()
# 3. Enviar MACs para o servidor
await huawei.enviar_macs(lista_mac)
# 4. Receber resposta do servidor
resposta = await huawei.receber_resposta()
# 5. Processar resposta
fluxoHuawei(resposta)
# 6. Fechar conexão com o servidor
await huawei.fechar_conexao()