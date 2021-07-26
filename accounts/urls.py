from django.contrib.auth import views
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), {'template_name': 'registration/logged_out.html'}, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]