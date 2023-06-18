from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = auth.authenticate(username=username1,password=password1)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Login successful')
            print("Login successful")
            return redirect('/')
        else:
            messages.info(request,'Password or username incorrect')
            print('Password or username incorrect')
            return redirect('login')
    return render(request,'login-test.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # if firstname is None:
        #     messages.info(request, "Fill username")
        #     return redirect("registration")
        # else:
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                print("Username taken")
                return redirect("registration")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                print("Email taken")
                return redirect("registration")
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                                last_name=lastname, email=email)
                user.save()
                print('User registered', username)
                return redirect('login')
        else:
            messages.info(request, "Pass not matching")
            print("Password not matching")
            return redirect("registration")
        return redirect('/')
    return render(request, 'registration.html')
