import os
import subprocess
from utils import get_admin_privileges

def install_programs(program_list, os_name):
    for program in program_list:
        print(f"Instalando {program}...")

        # Verificar si se tiene un enlace para descargar
        download_link = f"https://example.com/{program}.exe"  # Reemplazar con un enlace real
        
        if os_name == 'windows':
            # Descargar e instalar en Windows
            download_command = f"curl -L -o {program}.exe {download_link}"
            result = subprocess.run(download_command, shell=True)

            # Comprobar si la descarga fue exitosa
            if result.returncode != 0:
                print(f"Error al descargar {program} en Windows.")
                continue  # Salir del ciclo para este programa
            
            # Ejecutar la instalación con privilegios de administrador
            try:
                get_admin_privileges(f"{program}.exe")
            except Exception as e:
                print(f"Error al instalar {program} en Windows: {e}")
        
        elif os_name == 'parrot':
            # Descargar e instalar en Parrot OS
            download_command = f"wget -O {program}.deb {download_link}"
            result = subprocess.run(download_command, shell=True)

            # Comprobar si la descarga fue exitosa
            if result.returncode != 0:
                print(f"Error al descargar {program} en Parrot OS.")
                continue  # Salir del ciclo para este programa
            
            # Instalar el paquete usando sudo
            install_command = f"sudo dpkg -i {program}.deb"
            result = subprocess.run(install_command, shell=True)

            # Comprobar si la instalación fue exitosa
            if result.returncode != 0:
                print(f"Error al instalar {program} en Parrot OS. Puede que falten dependencias.")
                # Intentar arreglar dependencias automáticamente
                subprocess.run("sudo apt-get install -f", shell=True)
