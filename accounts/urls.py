from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterUser
# from .viewsets import MyObtainTokenPairView, RegisterViewSet
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('cadastro', RegisterUser.as_view(), name='register'),
    path('entrar/', auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
]
