# Auto Installer

## Description

This project consists of a task automation tool that allows you to scan the operating system to identify installed programs and facilitate the automatic installation of applications on Windows and Parrot OS.

## Features

- Scans the system to generate a list of installed programs.

- Loads settings from a JSON file.

- Automatically installs programs based on a list of preferences.

- Supports both Windows and Parrot OS.

## Project Structure

├── config.json # Configuration file with download links and programs

├── install_manager.py # Main script that manages scanning and installation

├── installer.py # Module to download and install programs

├── os_scan.py # Module to scan installed programs

└── utils.py # Utilities to manage permissions and auxiliary functions

## Requirements

- Python 3.x

- Libraries: `subprocess`, `os`, `json`, among others.

## Installation

1. Clone this repository to your machine:

```bash
git clone https://github.com/tobproject/auto_installer.git

cd auto_installer
```

2. Make sure you have curl (for Windows) and wget (for Parrot OS) installed on your system.

## Configuration

Edit the config.json file to add the programs you want to install. Make sure to include the program name, download URL, and corresponding operating system.

```json
{

"programs": [

{

"name": "Google Chrome",

"url": "https://dl.google.com/chrome/install.exe",

"os": "windows"

},

{

"name": "Firefox",

"search_query": "firefox download",

"os": "parrot"

}

]

}
```

## Usage

1. Run the main script:

```bash
python install_manager.py
```

2. The script will scan your system and generate an 'installed_programs.txt' file with the list of installed programs.

3. Based on the settings in the `config.json` file, it will automatically install programs in the preferred order.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

