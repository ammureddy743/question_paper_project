from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import UserRegistrationModel


# ---------------- BASIC PAGES ---------------- #
def index(request):
    return render(request, 'index.html')


def AdminLogin(request):
    return render(request, 'AdminLogin.html')


def UserLogin(request):
    return render(request, 'UserLogin.html')


def UserRegister(request):
    from users.forms import UserRegistrationForm
    form = UserRegistrationForm()
    return render(request, 'UserRegistration.html', {'form': form})


# ---------------- ADMIN LOGIN ---------------- #
def adminLoginCheck(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 🔐 Simple admin login (you can upgrade later)
        if username == "admin" and password == "admin":
            request.session['admin'] = True
            return redirect('AdminHome')
        else:
            messages.error(request, "Invalid admin login")

    return render(request, 'AdminLogin.html')


# ---------------- ADMIN HOME ---------------- #
def adminHome(request):
    if not request.session.get('admin'):
        return redirect('AdminLogin')

    return render(request, 'admins/AdminHome.html')


# ---------------- VIEW USERS ---------------- #
def RegisterUsersView(request):
    if not request.session.get('admin'):
        return redirect('AdminLogin')

    users = UserRegistrationModel.objects.all()
    return render(request, 'admins/view_users.html', {'users': users})


# ---------------- ACTIVATE USER ---------------- #
def activateUser(request, id):
    user = UserRegistrationModel.objects.get(id=id)
    user.status = "activated"
    user.save()
    return redirect('view_users')


# ---------------- DEACTIVATE USER ---------------- #
def DeactivateUsers(request, id):
    user = UserRegistrationModel.objects.get(id=id)
    user.status = "deactivated"
    user.save()
    return redirect('view_users')


# ---------------- DELETE USER ---------------- #
def deleteUser(request, id):
    UserRegistrationModel.objects.get(id=id).delete()
    return redirect('view_users')