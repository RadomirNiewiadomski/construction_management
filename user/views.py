from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


def is_admin(user):
    return user.role == 'ADMINISTRATOR'


@login_required
def user_dashboard(request):
    """User dashboard for normal users."""
    return render(request, "user_dashboard.html")


@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    """Admin dashboard for administrators."""
    return render(request, "admin_dashboard.html")


@user_passes_test(is_admin)
def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/create_user.html', {'form': form})


@user_passes_test(is_admin)
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'user/edit_user.html', {'form': form})


def login_view(request):
    """Custom login view."""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'ADMINISTRATOR':
                return redirect('user:admin_dashboard')
            return redirect('user:user_dashboard')
        else:
            return HttpResponse('Invalid credentials', status=401)
    return render(request, 'user/login.html')


def register_user(request):
    """Custom user registration view."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})


@user_passes_test(is_admin)
def user_list(request):
    """List all users for administrator."""
    users = User.objects.all()
    return render(request, 'user/user_list.html', {'users': users})


@user_passes_test(is_admin)
def delete_user(request, user_id):
    """Delete a user."""
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('user:user_list')
