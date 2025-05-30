from flask import Flask, render_template, request, jsonify
from scapy.all import ARP, Ether, srp
import time

app = Flask(__name__)

# Diccionario para almacenar el estado de los dispositivos
devices_status = {}

def scan_network(network_ip_range):
    arp_request = ARP(pdst=network_ip_range)
    ether_broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = ether_broadcast / arp_request

    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    current_devices = {}

    # Actualiza los dispositivos detectados en el escaneo actual
    for sent, received in answered_list:
        ip = received.psrc
        mac = received.hwsrc
        current_devices[ip] = mac

        # Marca como activo o agrega al diccionario
        devices_status[ip] = {'mac': mac, 'status': 'Activo'}

    # Detecta dispositivos que estaban activos y ya no responden en el escaneo actual
    for ip in list(devices_status.keys()):
        if ip not in current_devices:
            devices_status[ip]['status'] = 'Inactivo'

    return devices_status

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    network_ip_range = request.form['network_ip_range']
    start_time = time.time()
    
    # Realiza el escaneo y actualiza el estado de los dispositivos
    network_devices = scan_network(network_ip_range)
    
    end_time = time.time()
    scan_time = end_time - start_time
    
    return jsonify({'devices': network_devices, 'time': scan_time})

if __name__ == '__main__':
    app.run(debug=True)
