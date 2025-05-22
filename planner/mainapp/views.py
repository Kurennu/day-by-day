from django.shortcuts import render, get_object_or_404, redirect
from .models import User    
from .forms import RegisterForm, LoginForm

def manager_home(request, user_id):
    user = get_object_or_404(User, id=user_id)
    tasks = user.tasks.all().order_by('start_time')
    schedule = getattr(user, 'schedule', None)

    context = {
        'user': user,
        'tasks': tasks,
        'schedule': schedule,
    }
    return render(request, 'mainapp/index.html', context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'mainapp/register.html', {'form': form})


def login_view(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    return redirect('manager_home', user_id=user.id)
                else:
                    error = 'Неверный пароль'
            except User.DoesNotExist:
                error = 'Пользователь не найден'
    else:
        form = LoginForm()
    return render(request, 'mainapp/login.html', {'form': form, 'error': error})
