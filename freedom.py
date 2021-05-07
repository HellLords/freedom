import socket
import os
banner = """
 _____              ____                  
|  ___| __ ___  ___|  _ \  ___  _ __ ___  
| |_ | '__/ _ \/ _ \ | | |/ _ \| '_ ` _ \ 
|  _|| | |  __/  __/ |_| | (_) | | | | | |
|_|  |_|  \___|\___|____/ \___/|_| |_| |_|


      ..:HellLords:.. t.me/helllords

\033[32m\033[01mВписывайте только имя домена! 
Без доменной зоны !!!
Доменная зона (Пример .ru)\033[m

"""
domain_zone = ['ru','in','org','pw','com','su','site','fun','uk.com','рф','space','store','website','online']

os.system('clear')
print(banner)
name = input("[DOMAIN] : ").lower()
os.system('clear')
for domain in domain_zone:
	try:sock = socket.gethostbyname(f"{name}.{domain}")
	except:print(f"Домен: {name}.{domain} Свободен!")
print("\nEnd -->>")
input()

#tg t.me/helllords