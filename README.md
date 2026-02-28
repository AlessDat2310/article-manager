## ALESSANDRO DATURI MIRANDA
## A01773901

## INFOGRAFÍA DJANGO 
Proyecto Django Completo
Aplicación web desarrollada con Django que permite: Crear artículos, visualizar todos los artículos (y sus contenidos), editar artículos existentes, eliminar artículos y administración vía panel Django

Este proyecto documenta paso a paso la creación de un entorno virtual, proyecto, aplicación y configuración de base de datos y habilitación de URLs.

---

1. Creación de un entorno virtual

El entorno virtual permite aislar las dependencias del proyecto.

---

2. Creación del proyecto en Django

django-admin startproject article_manager

Y vinculación con la base de datos (en mi caso Sqlite)

Realizar la migración

---

3. Creación de la app y se guarda en Settings

INSTALLED_APPS = [
    ...
    'articles',
]

---

4. ESTRUCTURA DEL PROYECTO

article_manager/
│
├── manage.py
├── db.sqlite3
│
├── article_manager/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── articles/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    └── templates/
        └── articles/
            ├── list.html
            ├── detail.html
            ├── new_article_form.html
            └── edit.html

---

## Tecnologías utilizadas

- Python 3.12
- Django
- SQLite3
- HTML
- CSS básico

---
Referencias:

Django Software Foundation. (2024). Django documentation.
https://docs.djangoproject.com/en/stable/

DeepSeek. (2026). Diseño de interfaz cyberpunk NEO-TOKYO 
para aplicación Django [Código fuente HTML/CSS]. 
Asistencia de IA en tiempo real. https://www.deepseek.com/

OpenAI. (2026). ChatGPT (versión GPT-5) [Modelo de lenguaje]. https://chat.openai.com/

Mondragón Guadarrama, J. C. (2026). Construcción de software y toma de decisiones 
(Gpo 401) [Clase de licenciatura]. Tecnológico de Monterrey.

---

Autor
Aless Dat2310
Proyecto académico — 2026

