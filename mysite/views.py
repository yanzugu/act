from django.contrib.auth.forms import UserCreationForm # 新增
from django.shortcuts import render, redirect
from django.contrib import auth, messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("Errors", form.errors)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'registration/register.html', {'form':form})
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect('/')
    else:
        if username or password:
            messages.info(request, '錯誤的帳號或密碼')
        return render(request, 'login.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')