from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.viewers_map, name='mapa'),
    path('klienci', views.clients, name='klienci'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('logowanie', views.login_user, name='logowanie'),
    path('administrator', views.dashboard, name='administrator'),
    path('wyloguj', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='wyloguj'),
]

