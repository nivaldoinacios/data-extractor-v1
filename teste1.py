from utils import *

load_dotenv()

start = time.time()

connection = ConnectHandler(**AC6005)
connection.enable()

command = 'display access-user'

outputA = connection.send_command(command)
outputB = str(outputA)
output = outputA

#output[303:] essa posição imprime sem o cabeçalho
print(output)
