"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os.path import join
from django.contrib import admin
from django.urls import include, path

# root URLconf
# The include() function allows referencing other URLconfs (polls.urls config). Whenever Django encounters include()
# it chops off whatever part of the url matched up to that point and sends the remaining string to the included URLconf
# for further processing.
# The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (poll/urls.py)
# They can be placed under "/polls/" or under "/fun_polls/" or any other path root, and the app will still work.
# You should always use include() when you include other URL patterns admin.site.urls is the only exception to this.
urlpatterns = [path("admin/", admin.site.urls), path("polls/", include("polls.urls"))]

# The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.
# At this point, it's worth reviewing that these argument are for.

# path() argument: route
# route is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in urlpatterns
# and makes its way down the list comparing the requested URL against each pattern until it finds one that matches.

# path() argument: view
# When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and
# any "captured" values from the route as keyword arguments.

# path() argument: kwargs
# Arbitrary keyword arguments can be passed in a dictionary to the target view.

# path() argument: name
# Naming your URL lets you refer to unambiguously from elsewhere in Django, especially from within template
