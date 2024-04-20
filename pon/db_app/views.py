from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.http import JsonResponse


class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label='email')


class EmailSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('email', 'password')


def signup(request):
    if request.method == 'POST':
        form = EmailSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return JsonResponse({'success': 'Пользователь успешно создан'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'error': errors})
    else:
        return JsonResponse({'error': 'Метод запроса должен быть POST'})


def login(request):
    if request.method == 'POST':
        form = EmailLoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            return JsonResponse({'success': 'Аутентификация успешна'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'error': errors})
    else:
        return JsonResponse({'error': 'Метод запроса должен быть POST'})



