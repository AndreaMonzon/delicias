# Django Imports
# from django.urls import path

# # App Imports
# from . import views


# urlpatterns = [
#     path('',views.productos, name="Productos"),
    
# ]

from django.urls import path
from .import views
urlpatterns=[
    path('',views.productos, name="Productos"),
     path('<int:param>/', views.productos),
]