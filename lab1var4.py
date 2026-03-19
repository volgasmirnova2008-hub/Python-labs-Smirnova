from math import factorial
from itertools import permutations
import os
import shutil
import psutil
import subprocess

n = int(input('длина перестановки'))
v = list(range(1,n+1))

print('число перестановок', factorial(n))
print(list(permutations(v)))

#ЗАПИСЬ ФАЙЛА
b = ' '.join(map(str,list(permutations(v))))
with open ('перестановки.fasta', 'a') as file: #a - дозапись, w - перезапись
   file.write(b)


#НАСТРОЙКА ДОСТУПА К ФАЙЛУ
print('можно ли записывать файл',os.access(path = r'C:\Users\ks_71\Documents\python\перестановки.fasta', mode = os.W_OK))
#os.F_OK - объект существует, os.R_OK - доступен на чтение, os.W_OK - доступен на запись, os.X_OK - доступен на исполнение
os.chmod(path = r'C:\Users\ks_71\Documents\python\перестановки.fasta', mode = 0o777)
#0o777: Полный доступ для всех (чтение, запись, выполнение)
#0o755: Владелец — всё, группа/остальные — чтение и исполнение.
#0o644: Владелец — чтение/запись, группа/остальные — только чтение.
#0o600: Владелец — чтение/запись, остальные — нет доступа.
#0o444: Только чтение для всех.

#МОЖНО ЛИ ЗАПИСАТЬ В ПАПКУ
def filesavingave(pathfolder, pathfile):
    if not os.path.isdir(pathfolder):
        print('Папка не существует')
        return
    
    if not os.access(pathfolder, os.W_OK):
        print('Папка не доступна для записи')
        return
    
    disk = os.path.splitdrive(pathfolder)[0] + '\\'  # Получаем диск 
    free_space = shutil.disk_usage(disk).free
    file_size = os.path.getsize(pathfile)
    
    if free_space < file_size:
        print('Недостаточно места на диске')
        return
    
    print('Папка существует, доступна для записи и достаточно места')
   
filesavingave(r'C:\Users\ks_71\Documents\python', r'C:\Users\ks_71\Documents\python\перестановки.fasta')

#ПРОВЕРКА ПРАВИЛЬНОСТИ ЗАПИСИ ФАЙЛА
def cor_file_rec(file_name, data):
    try:
        try:
            with open(file_name, "r") as file:
                old_content = file.read()
        except FileNotFoundError:
            old_content = ""  # файла не было
        
        with open(file_name, "a") as file:
            file.write(data)
        
        with open(file_name, "r") as file:
            new_content = file.read()
        
        expected_new = old_content + data
        
        if new_content == expected_new:
            print("Файл записан успешно, проверка пройдена")
        else:
            print("Ошибка: Добавление произошло неправильно")
    
    except Exception as e: 
        print(f"ошибка: {e}")

cor_file_rec('перестановки.fasta', b)

#ОБРАЩЕНИЯ К ФАЙЛУ
def who_uses_file(path):
    result = subprocess.run(
        ["handle.exe", path],
        capture_output=True,
        text=True
    )
    return result.stdout

print(who_uses_file(r'C:\Users\ks_71\Documents\python\перестановки.fasta'))

#ДЛЯ СЕБЯ
print(os.getcwd()) #директория
#pip install psutil