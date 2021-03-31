from django.shortcuts import render
from django.http import HttpResponse
from .models import Strategy
from rest_framework import generics
from .serializers import StrategySerializer


def home(request):
    return render(request, "home.html", {
        "title": "Home"
    })


def create(request):
    if request.method == "GET":
        return render(request, "create-strategy.html", {
            "title": "Create Strategy"
        })
    elif request.method == "POST":
        body = request.POST


def test(request):
    return render(request, "test-strategy.html", {
        "title": "Test Strategy"
    })


def deploy(request):
    return render(request, "deploy-strategy.html", {
        "title": "Create Strategy"
    })


class StrategiesView(generics.ListAPIView):
    queryset = Strategy.objects.all()
    serializer_class = StrategySerializer
    success_url = "/"
