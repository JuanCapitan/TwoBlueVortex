def mostrar_banner():
    banner = """
\033[96m
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║  ████████╗██╗    ██╗ ██████╗ ██████╗ ██╗     ██╗   ██╗███████╗   ║
║  ╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║     ██║   ██║██╔════╝   ║
║     ██║   ██║ █╗ ██║██║   ██║██████╔╝██║     ██║   ██║█████╗     ║
║     ██║   ██║███╗██║██║   ██║██╔══██╗██║     ██║   ██║██╔══╝     ║
║     ██║   ╚███╔███╔╝╚██████╔╝██████╔╝███████╗╚██████╔╝███████╗   ║
║     ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝   ║
║                                                                  ║
║  ██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗             ║
║  ██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝             ║
║  ██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝              ║
║  ╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗              ║
║   ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗             ║
║    ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝             ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

         \033[94m[ Herramienta Profesional de Pruebas DDOS ]\033[0m
              \033[94m[ Creado por: TwoBlueVortex ]\033[0m
                    \033[94m[ Version: 2.0 ]\033[0m
    """
    print(banner)

def menu_principal():
    menu = """
\033[96m╔════════════════════ MENÚ PRINCIPAL ═══════════════════╗
║                                                        ║
║  [1] 🚀 Iniciar Ataque                                ║
║      └─ Lanzar ataque DDOS personalizado              ║
║                                                        ║
║  [2] 🔍 Análisis de Objetivo                          ║
║      └─ Escanear y analizar objetivo                  ║
║                                                        ║
║  [3] ⚙️  Configuración                                ║
║      └─ Ajustar parámetros del ataque                 ║
║                                                        ║
║  [4] 📊 Ver Reportes                                  ║
║      └─ Consultar estadísticas y logs                 ║
║                                                        ║
║  [5] ❓ Ayuda                                         ║
║      └─ Manual de uso y comandos                      ║
║                                                        ║
║  [6] 🚪 Salir                                         ║
║      └─ Cerrar programa                               ║
║                                                        ║
╚════════════════════════════════════════════════════════╝\033[0m

\033[94m[*]\033[0m Ingrese el número de la opción deseada: """
    return input(menu)
