
# Escáner de Red en Tiempo Real 🌐🖥️

Aplicación web desarrollada con Flask que permite escanear redes locales en tiempo real utilizando peticiones ARP. La herramienta identifica dispositivos activos e inactivos en un rango de direcciones IP y muestra los resultados a través de una interfaz web intuitiva.

## 📌 Descripción del Proyecto

Este escáner de red permite a los usuarios obtener una lista de dispositivos conectados a su red local, mostrando tanto su dirección IP como su dirección MAC. El sistema también indica si el dispositivo está activo o inactivo, según los resultados del escaneo actual.

## 🚀 Tecnologías Utilizadas

- **Flask** (Python)
- **Scapy** (para escaneo de red vía ARP)
- **HTML + CSS (Jinja templates)**
- **JavaScript**
- **Bootstrap (opcional para el frontend)**

## 🧠 Funcionalidades Principales

- Escaneo de red en tiempo real mediante protocolo ARP.
- Identificación de dispositivos activos e inactivos.
- Visualización clara y rápida en una interfaz web.
- Medición del tiempo total de escaneo.
- Actualización automática del estado de los dispositivos detectados.

## 🔍 Lógica del Escaneo

```python
arp_request = ARP(pdst=network_ip_range)
ether_broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
arp_request_broadcast = ether_broadcast / arp_request
answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]
```

## 🖥️ Interfaz Web

Desde la página principal (`/`), el usuario puede ingresar un rango IP (por ejemplo: `192.168.1.1/24`) y lanzar el escaneo. Los resultados se muestran como una lista de dispositivos con su IP, MAC y estado (`Activo` o `Inactivo`).

## ⚙️ Cómo Ejecutar

1. Instala dependencias:
```bash
pip install flask scapy
```

2. Ejecuta la app:
```bash
python app.py
```

3. Abre tu navegador en:
```
http://localhost:5000
```

## 👨‍💻 Autor

**Ruben Abimalec Caballero Sánchez**  
Desarrollador del backend y lógica de escaneo de red con Scapy.

## 🛡️ Nota Legal

Esta herramienta es para fines educativos y de diagnóstico en redes propias. No debe usarse para acceder a redes ajenas sin autorización.
