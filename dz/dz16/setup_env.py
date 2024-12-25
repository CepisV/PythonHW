import os
import subprocess
import sys

VENV_DIR = "venv"

def create_virtual_environment():
    if not os.path.exists(VENV_DIR):
        print("Создаю виртуальное окружение...")
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])
    else:
        print("Виртуальное окружение уже существует.")

def install_dependencies():
    print("Устанавливаю зависимости...")
    subprocess.check_call([os.path.join(VENV_DIR, "bin" if os.name != "nt" else "Scripts", "pip"), "install", "python-docx"])

if __name__ == "__main__":
    create_virtual_environment()
    install_dependencies()
    print("Установка завершена.")
