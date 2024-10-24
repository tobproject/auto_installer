import os
import subprocess

# Función para guardar la lista de programas en un archivo de texto
def save_installed_programs(installed_programs):
    try:
        with open('installed_programs.txt', 'w') as file:
            file.write("Programas instalados en el sistema:\n")
            for program in installed_programs:
                file.write(f"- {program}\n")
        print("Archivo 'installed_programs.txt' creado exitosamente.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

# Función para solicitar permisos de administrador en Windows
def get_admin_privileges(file_path):
    try:
        if os.name == 'nt':
            command = f"powershell Start-Process {file_path} -Verb runAs"
            subprocess.run(command, shell=True)
        else:
            print("Función de privilegios de administrador solo está disponible en Windows.")
    except Exception as e:
        print(f"Error al solicitar privilegios de administrador: {e}")
