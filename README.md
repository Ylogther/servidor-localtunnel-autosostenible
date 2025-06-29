# 🌐 Exponer un servidor Python local con LocalTunnel

[![License: MIT](https://img.shields.io/badge/Licencia-MIT-blue.svg)](LICENSE)
![Estado: Funcional](https://img.shields.io/badge/estado-funcional-brightgreen)
![Compatibilidad: Windows / Linux](https://img.shields.io/badge/compatibilidad-Windows%20%2F%20Linux-orange)
![Requiere: Node.js](https://img.shields.io/badge/requiere-Node.js-yellow)
![Uso: Python + LocalTunnel](https://img.shields.io/badge/uso-Python%20%2B%20LocalTunnel-informational)

---

## 📝 Descripción

Este proyecto te permite levantar un servidor HTTP simple con Python (puerto 3000) y **exponerlo a Internet** usando [LocalTunnel](https://github.com/localtunnel/localtunnel).  
Ideal para compartir archivos, pruebas web o hacer debugging remoto desde cualquier red sin configuración de puertos ni servidores externos.

---

## ⚙️ Requisitos

- Python 3 instalado
- Node.js + npm
- LocalTunnel instalado globalmente

---

## 🚀 Instalación paso a paso

### 🔹 Paso 1: Instalar Node.js

Ve a la página oficial:  
👉 https://nodejs.org/es

Descarga el instalador para tu sistema operativo (Windows o Linux) y ejecútalo.

Verifica en consola:

```bash
node -v
npm -v
````

---

### 🔹 Paso 2: Instalar LocalTunnel globalmente

```bash
npm install -g localtunnel
```

Esto instalará el comando `lt` disponible globalmente.

---

### 🔹 Paso 3: Levantar servidor HTTP

Desde el directorio donde tengas archivos que desees exponer, ejecuta:

```bash
python3 -m http.server 3000
```

Esto iniciará un servidor en `http://localhost:3000`.

---

### 🔹 Paso 4: Exponer con LocalTunnel

Abre otra terminal y ejecuta:

```bash
lt --port 3000 --subdomain NOMBRE
```

> Reemplaza `NOMBRE` con el subdominio que quieras (si está disponible).

Ejemplo:

```bash
lt --port 3000 --subdomain pruebascript
```

Resultado esperado:

```
your url is: https://pruebascript.loca.lt
```

Este enlace será accesible desde cualquier parte del mundo.

---

### ⚠️ Antes de iniciar el script verificador

Si tienes un archivo `verify_linux.py` o `verify_win.py`, asegúrate de editarlo y reemplazar el texto:

```python
# "pon tu subdominio"
```

por el subdominio que hayas elegido (sin `https://`).

---

## 🧪 Verificación

Ejecuta:

```bash
# En Linux:
python3 verify_linux.py

# En Windows:
python3 verify_win.py
```

---

## 📄 Licencia

Este proyecto está bajo la **[Licencia MIT](LICENSE)**.
Puedes usar, modificar y distribuir libremente.

---
