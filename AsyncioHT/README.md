---
title: 'Asyncio'
author: 'RMS83'
---
# Выгрузка из API персонажей Start Wars и загрузка в базу данных

## Шаги по запуску приложения.
Все команды выполнять в терминале
* клонируйте репозиторий с GitHub к себе на хост (Ваш PC)
* перейдите в директорию AsyncioHT
* создайте виртуальное окружение и установите зависимости из requirements.txt
* запустите оркестратор (в нем крутится БД) 
* запустите приложение (main.py)
```shell
git clone https://github.com/RMS83/PiWEB.git
cd PiWEB/AsyncioHT
python venv venv
./venv/Scripts/activate
pip install -r requirements.txt
docker-compose up
python main.py
```
