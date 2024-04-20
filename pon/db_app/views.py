from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from db_app.models import User
from django import forms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import json


class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')


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





@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']

            # Добавим отладочный вывод для проверки полученных данных
            print("Email:", email)
            print("Password:", password)

            # Используйте authenticate для аутентификации пользователя
            user = authenticate(request, email=email, password=password)

            if user is not None:
                # Пользователь аутентифицирован успешно
                return JsonResponse({'success': 'Аутентификация успешна'})
            else:
                # Неверные учетные данные
                return JsonResponse({'error': 'Неверные учетные данные'}, status=400)
        except KeyError:
            return JsonResponse({'error': 'Отсутствуют необходимые данные'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Метод запроса должен быть POST'}, status=405)

