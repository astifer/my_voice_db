### Цифровой прорыв. Всероссийский этап

Трек от Росатома для платформы мой голос

![rosatom](https://github.com/cradmlozzer/my_voice_db/assets/108126763/d762933e-c5a2-4ce8-893a-a9f318cb5b67)

Задача кластеризации вопросов и представление их в визуально понятном виде

![test](https://github.com/cradmlozzer/my_voice_db/assets/108126763/8bf7d462-a8bd-4d34-a64c-0c8d500e9d67)


# Решение и архитектура

## Архитектура

На вход поступает файл json и парсится. Для каждого ответа моделью Word2Vec(gensim) создается вектор ембедингов. Далее алгоритмом K-means с помощью Silhouette Method происходит кластеризация и создается итоговый файл. В нем каждому ответу сопоставляется текстовое описание класса, к которому принадлежит текс

![image-4](https://github.com/cradmlozzer/my_voice_db/assets/108126763/72bdeadf-8f2f-49d1-9c56-74ad0cf28fc2)

## Фильтр подозрительных слов

Как дополнителная фича нами была разработана модель детектирующая токсичные, грубые или сомнительные ответы

## Решение

Решение сейчас это демо версия сайта, доступная по следующему адресу:

[dafe-212-46-18-171](https://dafe-212-46-18-171.ngrok-free.app)

# Стек

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)