from pkg_resources import time, asyncio
from etl import (
    gerar_lista_mac,
    HuaweiTelnet,
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
    await asyncio.sleep(1)
    gerar_lista_mac(WorldItem.lista_stations)
    WorldItem.lista_mac = gerar_lista_mac(
        WorldItem.lista_stations
    )
    return WorldItem.lista_mac


async def steps():
    print(f'Iniciando o fluxo de steps {time.strftime("%H:%M:%S")}')

    first_task = asyncio.create_task(first_step())
    second_task = asyncio.create_task(second_step())
    third_task = asyncio.create_task(third_step())
    await first_task
    await second_task
    await third_task
    print(f'Finalizando o fluxo de steps {time.strftime("%H:%M:%S")}')

asyncio.run(steps())
#%%


WorldItem.lista_mac = gerar_lista_mac(WorldItem.lista_stations)
print(WorldItem.lista_mac)
#%%
async def third_step():
    await asyncio.sleep(1)
    gerar_lista_mac(WorldItem.lista_stations)
    WorldItem.lista_mac = gerar_lista_mac(
        WorldItem.lista_stations
    )
    return WorldItem.lista_mac
#%%
