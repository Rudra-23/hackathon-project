from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# password for test user is Harry$$$***000
# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'authlog/index.html')

def signupUser(request):
    if request.method == "POST":
        username = request.POST.get('doc_name')
        email = request.POST.get('doc_email')
        password = request.POST.get('doc_pass')
        user = User.objects.create_user(username,email , password)
        user.save()
    return render(request, 'authlog/login.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('user_name')
        password = request.POST.get('pass_word')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'authlog/login.html')
    return render(request, 'authlog/login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")
