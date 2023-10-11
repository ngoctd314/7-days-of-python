# Django

## Installation

After you've created and activated a virtual environment, enter the command:

```txt
python -m pip install Django
```

**Creating a project**

If this is your first time using Django, you'll have to take care of some initial setup. Namely, you'll need to auto-generate some code that establishes a Django project - a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.

```txt
├── manage.py
└── mysite
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

+ manage.py: A command-line utility that lets you interact with this Django project in various ways.
+ mysite: directory is the actual Python package for your project. Its name is the Python package name you'll need to use to import anything inside 
+ mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package.
+ mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
+ mysite/urls.py: The URL declarations for this Django project; a "table of contents" of your Django-powered site. You can read more about URLs is URL dispatcher.
+ mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your project.
+ mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you're storing. Django follows DRY principle. The goal is to define your data model in one place and automatically derive things from it.

```txt
python manage.py makemigrations polls
```

By running makemigrations, you're telling Django that you've made some changes to your models. 


