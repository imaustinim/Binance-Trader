from django.urls import path
from . import views
from .views import StrategiesView

urlpatterns = [
    path("", views.home, name='home'),
    path("strategy/", StrategiesView.as_view()),
    path("strategy/create", views.create, name="strategy"),
    path("strategy/test", views.test, name="strategy"),
    path("strategy/deploy", views.deploy, name="strategy"),
]
