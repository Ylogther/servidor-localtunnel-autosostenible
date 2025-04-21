ANTES DE INICIARLO SE TIENE QUE INSTALAR LOCALTUNNEL

Paso 1: 
Instalar Node.js
Ve al sitio oficial de Node.js y descarga el instalador para Windows:

https://nodejs.org/es

Ejecuta el instalador y sigue los pasos para completar la instalación.

Para verificar que Node.js y npm se instalaron correctamente, abre el Símbolo del sistema (cmd) o PowerShell y ejecuta:

node -v
npm -v

Deberías ver las versiones instaladas de Node.js y npm.

Paso 2: 
Instalar LocalTunnel
Abre el Símbolo del sistema (cmd) o PowerShell y ejecuta el siguiente comando para instalar LocalTunnel globalmente:

npm install -g localtunnel

Esto instalará LocalTunnel y te permitirá acceder al comando lt desde cualquier directorio.

antes de iniciarlo entra al archivo python que usaras y cambia la parte que dice pon tu subdominio pon el que quieras usar

PARA INICIAR EL ARCHIVO:

primero con python crea un servidor en el puerto 3000 con el comando:

python3 -m http.server 3000

ahora en otra ventana ejecuta esto:

python3 verify_linux.py

o el verify_win.py dependiendo el OS que tengas.
