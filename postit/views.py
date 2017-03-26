from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from postit.models import Postit

# Create your views here.
def home(request):
    if request.method == 'POST' and request.POST.get('message','') != '':
        Postit.objects.create(
            message = request.POST.get('message'),
            user = request.user if request.user.is_authenticated() else None
            )

    return render(request, 'home.html', context={
        'postit_list': Postit.objects.all().order_by('-created_at'),
    })

def login_page(request):
    error = None
    if request.method == "POST":
        user = authenticate(
            username = request.POST.get("username"),
            password = request.POST.get("password"),
        )

        if user is not None:
            #로그인 성공
            login(request, user)
            return redirect('/')
        else:
            #로그인 실패
            error = "로그인실패"
    return render(request, 'login.html', context={
        'error': error
    })