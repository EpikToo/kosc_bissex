from django.urls import path
from . import views

urlpatterns = [
    path('bissex_annee/', views.Bissex_annee),
    path('bissex_range/', views.Bissex_range),
    path('bissex_history/', views.Bissex_history),

]