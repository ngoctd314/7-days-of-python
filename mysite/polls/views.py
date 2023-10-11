from django.http import HttpResponse


# Create your views here.
def index(request, **kwargs):
    print("kwargs: ", kwargs)
    return HttpResponse(bytes("Hello Django", "utf-8"))
