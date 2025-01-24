# nmap_parse
Script en Python que mejora la salida de resultados de un escaneo con nmap y organiza los datos en un formato más legible. El script procesa el archivo generado con el comando -oG de nmap (como firstScanPorts)

#Cómo usar el script:

##1. Realizar el escaneo con nmap

> nmap -p- --open -sS -min-rate 5000 -vvv -n -Pn <IP Objetivo> -oG firstScanPorts
