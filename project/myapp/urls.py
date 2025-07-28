from django.urls import path 
from . import views
urlpatterns = [
    ## STEP 4 #
     path('estudiante', views.registrar_Estudiante),
]







