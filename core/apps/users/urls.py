from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView, name='user_login_view'),
    path('home/', views.HomeView, name='user_home_view'),
    path('admin/', views.AdminView, name='user_admin_view'),
    path('unauthorized_page/', views.UnauthorizedPageView, name='unauthorized_page'),
]