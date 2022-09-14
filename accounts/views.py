from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect
from .models import CustomUser


class RegisterUser(TemplateView):
    template_name = "register.html"
    
    def post(self, request, *args, **kwargs):
        
        user = CustomUser.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email")
        )
        user.set_password(request.POST.get("password"))
        user.save()
        return redirect("login")
