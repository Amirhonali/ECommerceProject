from django.urls import path
from core import views

app_name = 'bananas'
urlpatterns = [
    path('bananas/', views.index)
]