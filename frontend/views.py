from django.shortcuts import render, redirect


def index(request, *args, **kwargs):
    return render(request, "frontend/index.html")
