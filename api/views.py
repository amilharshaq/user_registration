from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json
import requests
from django.shortcuts import render



@csrf_exempt
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        errors = {}

        #validating the user inputs
      
        if not username or username.strip() == "":
            errors['username'] = ['This field is required.']
        elif User.objects.filter(username=username.strip()).exists():
            errors['username'] = ['This username is already taken.']

        if not email or email.strip() == "":
            errors['email'] = ['This field is required.']
        else:
            try:
                validate_email(email.strip())
                if User.objects.filter(email=email.strip()).exists():
                    errors['email'] = ['This email is already taken.']
            except ValidationError:
                errors['email'] = ['Enter a valid email address.']

        if not password or password.strip() == "":
            errors['password'] = ['This field is required.']
        elif len(password.strip()) < 6:
            errors['password'] = ['Password must be at least 6 characters.']


        if errors:
            return JsonResponse({
                'success': False,
                'errors': errors
            }, status=400)
        
        user = User.objects.create_user(username=username, email=email, password=password)

        # calling n8n web hook

        payload = {
            'username': username,
            'email': email
        }

        try:

            # the n8n web hook url is declared in settings.py, im using n8n for the first time and i have used their free cloud service for 14 days.

            n8n_url = settings.N8N_WEBHOOK_URL
            requests.post(n8n_url, json=payload, timeout=5)
        except Exception as e:
            print(f"n8n webhook error: {e}")

 
        return JsonResponse({
            'success': True,
            'message': 'Registration successful.'
        }, status=201)


    return JsonResponse({
        'success': False,
        'errors': 'Method not allowed.'
    }, status=405)
