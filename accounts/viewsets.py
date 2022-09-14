from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny

# from rest_framework_simplejwt.views import TokenObtainPairView

# from .serializers import MyTokenObtainPairSerializer, RegisterSerializer

# class MyObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     serializer_class = MyTokenObtainPairSerializer


# class RegisterViewSet(generics.CreateAPIView):
#     """
#     <strong>Description:</strong><br>
#     Creating users to access API functions, managing employees and viewing reports.
#     """

#     queryset = User.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = RegisterSerializer
