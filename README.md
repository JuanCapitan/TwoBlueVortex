# TwoBlueVortex - Herramienta Profesional DDOS

TwoBlueVortex es una herramienta avanzada diseñada para realizar ataques de Denegación de Servicio Distribuida (DDoS). La herramienta utiliza múltiples vectores de ataque para abrumar un servidor objetivo, aprovechando técnicas de evasión y optimización para simular una carga masiva en el sistema de destino.

Este proyecto es solo para pruebas educativas y en entornos controlados con permisos explícitos. El uso de esta herramienta en redes o servidores sin autorización es ilegal y está en contra de la ética del hacking.

Funcionalidades

Escaneo de Puertos y Análisis de Objetivos:

Verifica la disponibilidad de puertos abiertos en un servidor objetivo.
Detecta posibles servicios en ejecución y sus versiones.
Realiza un análisis completo del objetivo utilizando Nmap para descubrir vulnerabilidades potenciales.
Ataques DDoS Multivectoriales:

UDP Flood: Genera un tráfico masivo UDP para saturar el servidor.
SYN Flood: Utiliza el protocolo TCP para inundar el servidor con solicitudes de conexión.
DNS Amplification: Aprovecha servidores DNS abiertos para amplificar el tráfico hacia el objetivo.
HTTP Flood: Realiza múltiples solicitudes HTTP para sobrecargar el servidor web.
Slowloris: Mantiene conexiones abiertas para bloquear la capacidad del servidor para aceptar nuevas conexiones.
Evasión de WAF (Firewalls de Aplicación Web):

Implementa técnicas como la rotación de user-agents, ofuscación de headers, y fragmentación de paquetes para evitar la detección de firewalls.

Monitoreo en Tiempo Real:

Monitorea el estado de las conexiones exitosas y fallidas durante el ataque.
Muestra estadísticas en tiempo real sobre el progreso del ataque, el número de paquetes enviados, y las tasas de éxito.
Generación de Reportes:

Genera informes detallados en formato JSON con estadísticas del ataque y resultados del análisis de objetivos.
Requisitos
Para ejecutar TwoBlueVortex, necesitas tener Python 3.x instalado, junto con las siguientes dependencias:

Python 3.x
requests
nmap
scapy
fake_useragent
colorama
tqdm
multiprocessing
logging
argparse
json

Puedes instalar las dependencias necesarias ejecutando:

pip install -r requirements.txt

Instalación

Clonar el Repositorio:

Clona el repositorio de TwoBlueVortex en tu máquina local utilizando Git:

git clone https://github.com/tu_usuario/TwoBlueVortex.git
Configurar el Repositorio:

Navega hasta el directorio del proyecto:

cd TwoBlueVortex
Instalar Dependencias:

Asegúrate de tener las dependencias necesarias para que la herramienta funcione correctamente:

pip install -r requirements.txt
Configurar el archivo JSON (Opcional):

Puedes modificar el archivo de configuración config.json para agregar tus propios proxies, establecer límites de ancho de banda y otros parámetros predeterminados.

Uso
Ejecutar el Ataque DDoS
Puedes iniciar un ataque DDoS ejecutando la herramienta desde la terminal con los siguientes parámetros:

python ataque_ddos.py -o <IP_O_DOMINIO_DEL_OBJETIVO> -p <PUERTO> -m <TIPO_DE_ATAQUE> --distribuido --sigiloso
-o: Dirección IP o nombre de dominio del servidor objetivo (Obligatorio).
-p: Puerto de destino (por defecto es 80 para HTTP).
-m: Método de ataque (opciones: syn, udp, dns, http, slowloris).
--distribuido: Realiza un ataque distribuido utilizando múltiples vectores de ataque.
--sigiloso: Activa el modo sigiloso para ocultar el tráfico del ataque.

Ejemplo:

python ataque_ddos.py -o 192.168.0.90 -p 80 -m syn --distribuido
Este comando lanzará un ataque DDoS distribuido con el método SYN Flood al servidor en 192.168.0.90 en el puerto 80.

Ejemplo de Reporte Generado
Al finalizar el ataque, el sistema generará un informe detallado con estadísticas y resultados. Un ejemplo de los datos que incluye el reporte es el siguiente:

{
    "timestamp": "2024-11-25T14:30:45",
    "estadisticas": {
        "conexiones_exitosas": 25000,
        "conexiones_fallidas": 3000,
        "tasa_exito": 89.23
    },
    "objetivos": [
        {
            "ip": "192.168.0.90",
            "puertos_abiertos": [80, 443],
            "servicios": [
                {"puerto": 80, "nombre": "HTTP", "version": "Apache 2.4.41"},
                {"puerto": 443, "nombre": "HTTPS", "version": "Nginx 1.18.0"}
            ]
        }
    ],
    "duracion_ataque": "35 minutos"
}

Consideraciones Éticas

TwoBlueVortex está diseñado para ser utilizado exclusivamente en entornos de pruebas y con permisos explícitos de los propietarios de los servidores. El uso de esta herramienta en redes o servidores sin autorización es ilegal y va en contra de las leyes y la ética de la ciberseguridad.

Por favor, utiliza esta herramienta de manera responsable. Siempre obtén el permiso adecuado antes de realizar cualquier tipo de prueba de penetración o ataque.

Contribuciones

Si deseas contribuir al desarrollo de TwoBlueVortex, por favor sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b mi-nueva-funcionalidad).
Realiza tus cambios y asegúrate de que los tests pasen.
Haz un commit de tus cambios (git commit -am 'Añadir nueva funcionalidad').
Haz un push a tu rama (git push origin mi-nueva-funcionalidad).
Abre un pull request para que tus cambios sean revisados y fusionados.

Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

¡Gracias por usar TwoBlueVortex!

## Instalación

```bash
git clone https://github.com/tu-usuario/TwoBlueVortex.git
cd TwoBlueVortex
pip install -r requirements.txt
