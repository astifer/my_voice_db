# Цифровой прорыв. Всероссийский этап

Трек от Росатома для платформы "МойГолос"

![cc_hr](https://github.com/cradmlozzer/my_voice_db/assets/108126763/0203a81d-aef5-426e-bb03-215bd7f0699c)

Задача кластеризации вопросов и представление их в визуально понятном виде. Исходные данные в виде проекции векторов:

![test](https://github.com/cradmlozzer/my_voice_db/assets/108126763/23ccd42c-9ee8-4223-9e55-45cadc89a7aa)


# Решение и архитектура

## Архитектура

На вход поступает файл json и парсится. Для каждого ответа моделью Word2Vec(gensim) создается вектор ембедингов. Далее алгоритмом K-means с помощью Silhouette Method происходит кластеризация и создается итоговый файл. В нем каждому ответу сопоставляется текстовое описание класса, к которому принадлежит текст

![image-4](https://github.com/cradmlozzer/my_voice_db/assets/108126763/72bdeadf-8f2f-49d1-9c56-74ad0cf28fc2)

## Фильтр подозрительных слов

Как дополнителная фича нами была разработана модель детектирующая токсичные, грубые или сомнительные ответы. Обучение происходило на датасете из открытого доступа

## Решение

Решение сейчас это демо версия сайта, доступная по следующему адресу:

[ngrok-free.app](https://72ef-91-207-7-77.ngrok-free.app)

![adress (2)](https://github.com/cradmlozzer/my_voice_db/assets/108126763/f554c4e6-7c5b-4542-8142-b6ac0ae8bcc7)

# Запуск

```
pip install -r requirements.txt
uvicorn back.app.main:app —reload —port 80


npm install
npm run dev
```

# Стек

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)


# Команда

>[Тимур, Backend&ML](https://t.me/goddesu)

>[Артём, ML](https://t.me/cradm_lozzer)

>[Аян, Frontend](https://t.me/vladtesla)

>[Вика, Design](https://t.me/victoriaburnasheva)
