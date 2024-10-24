import os
import platform
import json
from os_scan import scan_installed_programs
from installer import install_programs
from utils import save_installed_programs

# Función para cargar configuraciones
def load_config(filename='config.json'):
    with open(filename, 'r') as file:
        return json.load(file)

# Función principal
def main():
    # Cargar configuraciones
    config = load_config()
    print("Configuraciones cargadas:", config)  # Imprime las configuraciones cargadas
    
    # Detectar sistema operativo
    current_os = platform.system().lower()
    print(f"Sistema operativo detectado: {current_os}")  # Mensaje de depuración
    if current_os == 'linux':
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release') as f:
                if 'parrot' in f.read().lower():
                    current_os = 'parrot'
    
    # Escanear programas instalados
    print("Escaneando programas instalados...")  # Mensaje de depuración
    installed_programs = scan_installed_programs(current_os)
    print(f"Programas encontrados: {installed_programs}")  # Mostrar lista en consola
    
    # Guardar lista en un archivo
    save_installed_programs(installed_programs)
    
    # Mostrar lista en consola
    print("Programas instalados guardados en 'installed_programs.txt'.")
    
    # Filtrar programas según el sistema operativo
    preferred_programs = []
    for program in config["programs"]:
        if program["os"] == current_os:
            preferred_programs.append(program)

    # Instalación de programas en orden de preferencia
    install_programs(preferred_programs, current_os)

if __name__ == "__main__":
    main()
