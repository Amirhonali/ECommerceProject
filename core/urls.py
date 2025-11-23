from django.urls import path
from core import panties

app_name = 'core'
urlpatterns = [
    path('', panties.index)
]