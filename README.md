**ALESSANDRO DATURI MIRANDA**
**A01773901**

# INFOGRAFÍA DJANGO

**Proyecto Django Completo**
Aplicación web desarrollada con Django que permite: Crear artículos, visualizar todos los artículos (y sus contenidos), editar artículos existentes, eliminar artículos y administración vía panel Django.

Este proyecto documenta paso a paso la creación de un entorno virtual, proyecto, aplicación y configuración de base de datos y habilitación de URLs.

---

## 0. Creación de un entorno virtual
El entorno virtual permite aislar las dependencias del proyecto.

COMANDO: env\Scripts\activate

Instalar Django
COMANDO: pip install django

---

## 1. Creación de un Proyecto en Django

Crear proyecto
COMANDO: django-admin startproject article_manager

Entrar al proyecto
COMANDO: cd article_manager

Ejecutar migraciones iniciales
COMANDO: python manage.py migrate

Base de datos habilitada
Como Django usa SQLite por defecto:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SQLite queda activada tras la migración.

---

## 2. Creación de una App en Django

COMANDO: python manage.py startapp articles

Registrar app en settings.py
INSTALLED_APPS = [ ... 'articles', ]

---

## 3. Estructura del Proyecto

article_manager/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
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

Archivos clave

Archivo: Función
models.py: Define las entidades
views.py: Lógica del servidor
urls.py: Rutas del sistema
templates/: Renderizado HTML
settings.py: Configuración global

---

## 4. Probar modificaciones

Cuando se modifica:

python manage.py makemigrations
python manage.py migrate

Ejecutar servidor
python manage.py runserver

Abrir en navegador: http://localhost:8000/

---

## 5. URL que muestra todas las entidades

Modelo (models.py)

class Article(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()

Vista (views.py)

def article_list(request):
    articles = Article.objects.all()
    return render(request, "articles/list.html", {"articles": articles})

URL (articles/urls.py)

path('', article_list, name='article-list'),

Template (list.html)

<h1>Lista de artículos</h1>
{% for article in articles %}
    <h2>{{ article.name }}</h2>
    <p>{{ article.content }}</p>
{% endfor %}

Resultado: Una página que muestra todas las entidades almacenadas en la base de datos.

---

## 6. URL que genera una nueva entidad

Vista

def article_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        content = request.POST.get("content")
        Article.objects.create(name=name, content=content)
        return redirect("article-list")
    
    return render(request, "articles/new_article_form.html")

URL

path('new/', article_create, name='article-create'),

Template

<form method="post">
    {% csrf_token %}
    <input type="text" name="name" placeholder="Título">
    <textarea name="content" placeholder="Contenido"></textarea>
    <button type="submit">Guardar</button>
</form>

---

## 7. RECURSOS

- Python 3.12
- Django
- SQLite3
- HTML
- CSS

---

## 8. Referencias

Django Software Foundation. (2024). Django documentation. https://docs.djangoproject.com/en/stable/

DeepSeek. (2026). Diseño de interfaz cyberpunk NEO-TOKYO para aplicación Django [Código fuente HTML/CSS]. Asistencia de IA en tiempo real. https://www.deepseek.com/

OpenAI. (2026). ChatGPT (versión GPT-5) [Modelo de lenguaje]. https://chat.openai.com/

Mondragón Guadarrama, J. C. (2026). Construcción de software y toma de decisiones (Gpo 401) [Clase de licenciatura]. Tecnológico de Monterrey.

---

## 9. Autor

AlessDat2310
Proyecto académico — 2026