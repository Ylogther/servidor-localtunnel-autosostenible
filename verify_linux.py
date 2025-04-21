import subprocess
import time
import requests

# URL para verificar si el servidor está conectado
CHECK_URL = "http://localhost:3000"  # Cambia a la URL del servidor a verificar

# Comando para iniciar LocalTunnel
LOCAL_TUNNEL_CMD = ["lt", "--port", "3000", "--subdomain", "pon-subdominio"]

# Función para verificar si el servidor está conectado
def is_server_connected():
    try:
        response = requests.get(CHECK_URL)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

# Función para reiniciar el servidor y lanzar LocalTunnel
def restart_server_and_localtunnel():
    # Comando para reiniciar el servidor (puede variar según tu sistema)
    # Asegúrate de que el usuario tenga permisos para reiniciar el servidor
    print("Reiniciando el servidor...")
    subprocess.run(["sudo", "systemctl", "restart", "your-server.service"])  # Cambia "your-server.service" por el nombre real

    # Espera unos segundos para permitir el reinicio
    time.sleep(10)

    # Ejecuta LocalTunnel
    print("Lanzando LocalTunnel en puerto 3000 con subdominio 'tu-subdominio'...")
    subprocess.Popen(LOCAL_TUNNEL_CMD)

def main():
    # Ejecutar LocalTunnel inicialmente
    subprocess.Popen(LOCAL_TUNNEL_CMD)

    while True:
        if is_server_connected():
            print("El servidor está conectado. Verificando nuevamente en 5 minutos...")
        else:
            print("El servidor no está conectado. Reiniciando...")
            restart_server_and_localtunnel()

        # Esperar 5 minutos antes de la próxima verificación
        time.sleep(300)

if __name__ == "__main__":
    main()
