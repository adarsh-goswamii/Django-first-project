from django.urls import path
from . import views

urlpatterns = [
  path("<int:month>", views.getMonth),    
  path("<str:month>", views.getChallenge),    
]