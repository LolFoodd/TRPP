# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Указываем переменные окружения
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Открываем порт для Flask
EXPOSE 5000

# Запускаем приложение
CMD ["flask", "run", "--host=0.0.0.0"]
