from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {} )

def contact(request, *args, **kwargs):
    print(request.user)
    contacts_context = {
        "name": "Harun",
        "number": 23,
        "list_contacts": [245, 564, 278, 344],

    }
    return render(request, "contact.html", contacts_context )

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {} )