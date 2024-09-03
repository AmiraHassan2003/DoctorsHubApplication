from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User

def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        if username and email and password:
            dataUser = User(userName = username, userEmail = email, userPassword = password)
            dataUser.save()
            return redirect('../')
        else:
            messages.error(request, "Username and email and Password are required.")
    return render(request, 'Registration/signUp.html')


def logIn(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        if email and password:
            dataUser = User.objects.filter(userEmail=email, userPassword = password)
            if dataUser.exists():
                if dataUser[0].userId:
                    context = {'user': dataUser}
                    # print("userrrrrr: ", dataUser[0].userId)
                    return render(request, 'Doctors/index.html', context)
            
            else:
                context = {'error': "InvalidUser"}
                return render(request, 'Registration/logIn.html', context)

    return render(request, 'Registration/logIn.html')

def logOut(request):
    return redirect('login')

def Home(request, user_id):
    user = User.objects.get(userId = user_id)
    if user is not None:
        context = {
            'user' : user,
        }

    return render(request, 'Doctors/index.html', context)
    

# Create your views here.
