import subprocess
import time
import requests
import shutil
import sys
import os
import signal

CHECK_URL = "http://localhost:3000"
LOCAL_TUNNEL_CMD = ["lt", "--port", "3000", "--subdomain", "pon-subdominio"]
SERVICE_NAME = "your-server.service"

def is_server_connected():
    try:
        response = requests.get(CHECK_URL, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def kill_existing_lt():
    try:
        output = subprocess.check_output(["pgrep", "-f", "lt"]).decode().strip().splitlines()
        for pid in output:
            print(f"Matando instancia previa de LocalTunnel (PID: {pid})")
            os.kill(int(pid), signal.SIGTERM)
    except subprocess.CalledProcessError:
        pass  # No hay procesos de lt corriendo

def restart_server_and_localtunnel():
    print("Reiniciando servicio:", SERVICE_NAME)
    subprocess.run(["sudo", "systemctl", "restart", SERVICE_NAME], check=False)
    time.sleep(5)
    kill_existing_lt()
    print("Lanzando LocalTunnel...")
    subprocess.Popen(LOCAL_TUNNEL_CMD)

def main():
    if shutil.which("lt") is None:
        sys.exit("❌ Error: 'lt' no está en el PATH. Instala localtunnel con: sudo npm install -g localtunnel")

    print("Inicializando verificación de servidor...")

    kill_existing_lt()
    subprocess.Popen(LOCAL_TUNNEL_CMD)

    while True:
        if is_server_connected():
            print("✅ Servidor activo. Próxima verificación en 5 minutos.")
        else:
            print("⚠️ Servidor no responde. Intentando reiniciar...")
            restart_server_and_localtunnel()

        time.sleep(300)

if __name__ == "__main__":
    main()
