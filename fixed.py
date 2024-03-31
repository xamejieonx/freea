import os
import sys
import time
import pyautogui
import requests
import atexit
from colorama import Fore, Back, Style
from datetime import datetime
import json
import ctypes  # Импортируем модуль ctypes

print("By xamejieon1337")
print("Build: Free, Verstion: 0.2")


def download_from_github(url, filename):
    # Получаем путь к директории, где находится текущий скрипт
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Создаем полный путь к файлу
    full_path = os.path.join(dir_path, filename)

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(full_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        # Регистрируем функцию для удаления файла при завершении скрипта
        atexit.register(os.remove, full_path)
    else:
        print(f"Ошибка при загрузке файла: {response.status_code}")

# Пример использования
url = 'https://github.com/xamejieonx/prem123/raw/main/scrimer.mp4'
filename = 'scrimer.mp4'
download_from_github(url, filename)

print("Файл со скримером успешно прочитался! ❤️")

# Проверяем, запущена ли программа от имени администратора
if not ctypes.windll.shell32.IsUserAnAdmin():
    print("Запустите программу с правами администратора.")
    time.sleep(5)
    sys.exit()

def find_file_in_same_directory(file_name):
    if getattr(sys, 'frozen', False):
        # Если программа запущена как исполняемый файл (exe)
        directory = os.path.dirname(sys.executable)
    else:
        # Если программа запущена как скрипт (.py)
        directory = os.path.dirname(os.path.realpath(__file__))
    
    for root, dirs, files in os.walk(directory):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

def open_file_and_press_f11(file_path):
    os.startfile(file_path)
    time.sleep(1)  # Пауза в 1 секунду
    pyautogui.press('f11')  # Нажимаем клавишу F11

def open_file_with_limit(file_path, daily_limit=1, scream_limit=2):
    usage_file = 'C:\\Windows\\System32\\usage.json'  # Изменено здесь
    if not os.path.exists(usage_file):  # Изменено здесь
        # Если файл использования не найден, создаем его
        with open(usage_file, 'w') as f:
            json.dump({'last_used': None, 'times_used_today': 0, 'screams_today': 0}, f)
    with open(usage_file, 'r+') as f:  # Изменено здесь
        usage_data = json.load(f)
        last_used = usage_data.get('last_used')
        times_used_today = usage_data.get('times_used_today')
        screams_today = usage_data.get('screams_today')
        today = datetime.now().strftime('%Y-%m-%d')
        if last_used == today:
            if times_used_today >= daily_limit:
                print("Лимит использования скрипта на сегодня исчерпан.")
                return
            elif screams_today >= scream_limit:
                print("Вы исчерпали лимит.")  # Изменено здесь
                time.sleep(20)  # Изменено здесь
                sys.exit()  # Изменено здесь
        else:
            # Сброс счетчиков, если новый день
            usage_data['last_used'] = today
            usage_data['times_used_today'] = 0
            usage_data['screams_today'] = 0
        # Увеличиваем счетчик использования скрипта и скримеров
        usage_data['times_used_today'] += 1
        usage_data['screams_today'] += 1
        f.seek(0)
        f.truncate()
        json.dump(usage_data, f)
    # Запускаем скример не более двух раз
    for _ in range(scream_limit):
        open_file_and_press_f11(file_path)
        time.sleep(120)  # Пауза в 2 минуты

file_name = 'scrimer.mp4'
file_path = find_file_in_same_directory(file_name)
if file_path is None:
    print(f"Файл {file_name} не найден.")
else:
    print(f"Файл {file_name} найден по пути: {file_path}")
    open_file_with_limit(file_path)
