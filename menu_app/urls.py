from django.urls import path
from menu_app.views import menu_view

urlpatterns = [
   path('menu/<str:name>/', menu_view, name='menu_view'),

]
