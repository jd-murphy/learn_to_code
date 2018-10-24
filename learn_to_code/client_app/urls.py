from django.urls import path
from client_app import views

app_name = 'client_app'
urlpatterns = [
    path('client_registration/', views.client_registration, name='client_registration'),
    path('client_login/', views.client_login, name='client_login'),
    path('client_logout/', views.client_logout, name='client_logout'),
    path('code/', views.code, name='client_code'),
    path('lessons/', views.lessons, name='client_lessons'),
]