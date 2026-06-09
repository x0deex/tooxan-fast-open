import pyautogui
import subprocess
import time
"""

    Russia:
    ВАЖНО ПЕРЕД ЗАПУСКОМ ЗАМЕНИТЬ: "login" и "password" на реальные данные для входа в Tooxan,
    путь к файлу "path_to_app"  скачать все модули прописав команду: pip install -r requirements.txt
    и уже смело можно ЗАПУСКАТЬ СКРИПТ...
    
    English:
    IMPORTANT BEFORE RUNNING: Replace 'login' and 'password' with your actual login credentials in Tooxan, 
    replace the file path 'path_to_app' with the correct path, 
    download all modules by running the command: pip install -r requirements.txt
    And then you can safely RUN THE SCRIPT...

"""

login = "Your_Username"
password = "Your_Password"

"""
    Путь к исполняемому файлу программы
    # Например: path_to_app = r"D:\MyApp\Tooxan.exe"
"""                                             # English
path_to_app = r"C:\Путь\К\Вашей\Программе.exe"  # <-- CHANGE THIS PATH TO WHERE 
                                                # THE Tooxan EXE FILE ITSELF IS LOCATED!

# Запускаем программу
subprocess.Popen(path_to_app)

"""
    Russia:
    Подберите время экспериментально, 
    для надежности лучше увеличить
    Я обычно ставлю на 5-3 секунды

    English:
    Determine the time experimentally; 
    for reliability, it is better to increase it.
    I usually set it to 5–3 seconds.
"""
time.sleep(5) # <--ЗАМЕНИ ЕСЛИ ХОЧЕШЬ: чтоб запускался быстрее(медленнее)

pyautogui.write(login)
pyautogui.press('enter')
pyautogui.write(password)
pyautogui.press('enter')

print("Данные для входа отправлены.\n(Подождиде запускаем Tooxan)")
