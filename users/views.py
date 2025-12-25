from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .serializers import RegisterSerializer

# ===== API РЕГИСТРАЦИЯ (JWT / REST) =====
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]



# ===== WEB РЕГИСТРАЦИЯ (HTML) =====
def register_view(request):
    if request.user.is_authenticated:
        return redirect('task-list-page')  # после успешной авторизации направляем на страничку личного кабинета task-list-page
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автологин
            return redirect("task-list-page")  # после регистрации направляем на страничку личного кабинета task-list-page
    else:
        form = UserCreationForm()
        
    return render(request, "registration/register.html", {"form": form})