from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

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
            return Response({
                'success': False,
                'errors': errors
            }, status=status.HTTP_400_BAD_REQUEST)

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

        return Response({
            'success': True,
            'message': 'Registration successful.'
        }, status=status.HTTP_201_CREATED)
