import socket
import os

try:sock = socket.gethostbyname("google.com")
except: print("Отсутствует интернет соединение!")

banner = """
 _____              ____                  
|  ___| __ ___  ___|  _ \  ___  _ __ ___  
| |_ | '__/ _ \/ _ \ | | |/ _ \| '_ ` _ \ 
|  _|| | |  __/  __/ |_| | (_) | | | | | |
|_|  |_|  \___|\___|____/ \___/|_| |_| |_|


   ..:HellLords:.. t.me/helllords v1.1

\033[32m\033[01mВписывайте только имя домена! 
Без доменной зоны !!!
Доменная зона (Пример .ru)\033[m

"""
domain_zone = ['ru','in','org','pw','com','su','site','fun','uk.com','рф','space','store','website','online']

os.system('clear')
print(banner)
name = input("[DOMAIN] : ").lower()
os.system('clear')
print("Ожидайте надписи End...\n")
for domain in domain_zone:
	try:sock = socket.gethostbyname(f"{name}.{domain}")
	except:print(f"Домен: {name}.{domain} Свободен!")
print("\nEnd: tap to Enter-->>")
input()

#tg t.me/helllords
