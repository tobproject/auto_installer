import os
import subprocess

def scan_installed_programs(os_name):
    installed_programs = []
    
    if os_name == 'windows':
        # Comando para listar programas instalados en Windows
        command = 'powershell "Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        installed_programs = [line.strip() for line in result.stdout.split('\n') if line.strip() and "DisplayName" not in line]
    
    elif os_name == 'parrot':
        # Comando para listar paquetes instalados en Parrot OS
        command = 'dpkg-query -W -f=\'${binary:Package}\n\''
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        installed_programs = result.stdout.split('\n')
    
    return installed_programs
