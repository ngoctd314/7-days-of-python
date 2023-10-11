# Day 4

## Working with APIs

## Getting Started With Django

Django is Python's most popular web framework, a set of tools designed for building interactive web applications. In this chapter, you'll learn how to use Django to build a project called learning Log, an online journal system that lets you keep track of information you've learned about different topics.

Django can respond to page requests and make it easier to read and write to a database, manage users, and much more.

### Setting Up a Project

When starting work on something as significant as a web app, you first need to describe the project's goals in a specification, or spec. Once you have a clear set of goals, you can start to identify manageable tasks to achieve those goals.

We'll write spec for Learning Log and start working on the first phase of the project. This will involve setting up a venv and building out the intial aspects of a Django project.

**Writing a Spec**

A full spec details the project goals, describes the project's functionality, and discusses its appearance and user interface. Like any good project or business plan, a spec should keep you focused and help keep your project on track. We won't write a full project spec here, but we'll layout a few clear goals to keep  the development process focused. Here's the spec we'll use:

We'll write a web app called Learning Log that allows users to log the topics they're interested in and make journal entries as they learn about each topic. The Learning Log home page will describe the site and invite users to either register or login. Once logged in, a user can create new topics, add new entries, and read and edit existing entries.

**Creating a Virtual Environment**

To work with Django, we'll first set up a virtual environment. A virtual environment is a place on your system where you can install packages and isolate them from other Python packages.

**Installing Django**

With the virtual environment activated, enter the following to update pip and install Django:

```txt
pip install --upgrade pip
pip install django
```

Because it downloads resources from a variety of sources, pip is upgraded fairly often. It's a good idea to upgrade pip whenever you make a new virtual environment.

**Creating a Project in Django**

Without leaving the active virtual environment, enter the following commands to create a new project:

```sh
django-admin startproject ll_project .
```

The startproject command tells Django to set up a new project called ll_project. The dot (.) at the end of the command creates the new project with a directory structure that will make it easy to deploy the app to a server when we're finished developing it.

manage.py: which is a short program that takes in commands and feeds them to the relevant part of Django. We'll use these commands to manages tasks, such as working with databases and running servers.

settings.py: controls how Django interacts with your system and manages your project.

urls.py: tells Django which pages to build in response to browser requests.

wsgi.py: Web server gateway inferface helps Django serve the file it creates.

**Creating the Database**

Django stores most of the information for a project in a database, so next we need to create a database that Django can work with.

**Viewing the Project**

python manage.py runserver

**Starting an App**

A Django project is organized as a group of individual apps that work together to make the project work as a whole. For now, we'll create one app to do most of our project's work.

```txt
python manage.py startapp learning_logs
```

The command startapp appname tells Django to create the infrastructure needed to build an app. When you look in the project directory now.

The most important files are models.py, admin.py and views.py.

**Defining Models**


