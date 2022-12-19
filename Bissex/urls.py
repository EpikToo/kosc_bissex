from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.Bissex_history),
]