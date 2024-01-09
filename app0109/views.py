from django.shortcuts import render


def home(request):
    return render(request, '0109_django_notes.html', {})


