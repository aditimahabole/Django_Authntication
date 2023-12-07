from django.urls import path
from .views import signup, user_login , dashboard

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]
