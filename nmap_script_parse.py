import re

def parse_nmap_output(file_path):
    """
    Procesa un archivo de salida de Nmap en formato grepable (-oG) y muestra los puertos abiertos.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        results = {}
        for line in lines:
            if "Ports:" in line:
                # Extraer la IP
                ip_match = re.search(r'Host: ([\d\.]+)', line)
                ip = ip_match.group(1) if ip_match else "Desconocida"
                
                # Extraer los puertos abiertos
                ports_info = re.search(r'Ports: (.+)', line)
                if ports_info:
                    ports = []
                    for port in ports_info.group(1).split(','):
                        port_details = port.strip().split('/')
                        if len(port_details) > 1 and port_details[1] == 'open':
                            ports.append({
                                'port': port_details[0],
                                'protocol': port_details[2],
                                'service': port_details[4],
                            })
                    results[ip] = ports
        
        # Formatear la salida
        for ip, ports in results.items():
            print(f"\n[+] Resultados para {ip}:")
            for port in ports:
                print(f"    - Puerto: {port['port']}, Protocolo: {port['protocol']}, Servicio: {port['service']}")
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {file_path}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ruta del archivo generado por nmap
nmap_output_file = "firstScanPorts"

# Llamar a la función para procesar el archivo
parse_nmap_output(nmap_output_file)
