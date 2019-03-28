
from django.urls import path,include
from .views import ListfinderView


urlpatterns = [
  
    path('', ListfinderView.as_view())
]