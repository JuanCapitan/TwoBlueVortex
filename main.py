from src.banner import mostrar_banner, menu_principal
from src.attack import AtaqueDDOSPro
from src.utils import procesar_opcion
import colorama

def main():
    colorama.init()
    mostrar_banner()

    while True:
        opcion = menu_principal()
        procesar_opcion(opcion)

if __name__ == "__main__":
    main()
