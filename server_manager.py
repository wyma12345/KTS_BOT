from server import Server
# Получаем из config.py наш api-token
from config import main_token


server1 = Server(main_token, 202481467, "server1")

server1.start()
