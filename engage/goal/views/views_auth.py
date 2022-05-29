from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

from goal.middleware import login_exempt

from ..models import Users


@login_exempt
def loginUser(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print('user login successful')
            return redirect('/goal')
        else:
            print('user login failed')
            return render(request, 'goal/login.html')

    return render(request, 'goal/login.html')


@login_exempt
def register(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        country = request.POST.get('country')
        dob = request.POST.get('dob')

        user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()

        userM = Users(
            username=username, password=password, email=email, first_name=first_name,
            last_name=last_name, phone=phone, city=city, country=country, dob=dob)

        userM.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/goal')
    return render(request, 'goal/register.html')


@login_exempt
def logoutUser(request):
    logout(request)
    return render(request, 'goal/logout.html')
