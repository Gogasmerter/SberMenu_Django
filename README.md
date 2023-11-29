# SberMenu

## Запуск проекта в dev-режиме

### Установите виртуальное окружение

 ```bash
python -m venv venv
```

### Активируйте виртуальное окружение

```bash
source venv/bin/activate
```
В Windows комманда активации будет отличаться:
```bat
venv\Scripts\activate
```

### Установите зависимости

* Для разработки установите зависимости из файла requirements/dev.txt
    ```shell
    pip install -r requirements/dev.txt
    ```

* Для тестирования установите зависимости из файла requirements/test.txt
    ```shell
    pip install -r requirements/test.txt
    ```
* Для прода установите зависимости из файла requirements/prod.txt
    ```shell
    pip install -r requirements/prod.txt
    ```

### Создайте в корневой папке файл ".env"

```bash
cp .env.template .env
```

В Windows комманда копирования будет отличаться:

```bat
copy template.env .env
```

#### Значения в .env

1. DJANGO_SECRET_KEY - секретный ключ, строка (DJANGO_SECRET_KEY="secret-key")
2. DJANGO_DEBUG - режим разработки, пустая строка, если False (DJANGO_DEBUG="")
3. DJANGO_ALLOWED_HOSTS - разрешенные хосты, список хостов разделённый "," (DJANGO_ALLOWED_HOSTS="127.0.0.1,localhost")

### Перейдите в папку проекта

```bash
cd SberMenu
```

### Создание Базы данных

#### Применить миграции

```bash
python manage.py migrate
```

### Запустите сервер

```bash
python manage.py runserver
```