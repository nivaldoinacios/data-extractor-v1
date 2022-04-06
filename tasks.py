import asyncio
from etl import (
    HuaweiTelnet,
    fluxoHuawei,
    WorldItem,
)

stepIn = fluxoHuawei()

stepIn.display_access_users()

stepIn.display_station_all()