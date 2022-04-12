from pkg_rsrcs import *


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

exec(open("utils.py").read())

exec(open("etl.py").read())

exec(open("actions.py").read())
