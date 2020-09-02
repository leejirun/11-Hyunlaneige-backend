import json, requests, os, re
import traceback
import bcrypt
import jwt
import my_settings

from django.views           import View
from django.http            import JsonResponse, HttpResponse
from django.shortcuts       import redirect

from hyunlaneige.settings   import SECRET_KEY
from .validators            import password_validation_function, phone_number_validation_function
from .models                import User

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not(password_validation_function(data['password'])):
                return JsonResponse({'message' : 'Incorrect Password Format'}, status = 400)
            if not(phone_number_validation_function(data['phone_number'])):
                return JsonResponse({'message' : 'Incorrect Phone_number Format'}, status = 400)
            if User.objects.filter(identifier = data['identifier']).exists():
                return JsonResponse({"message" : "Already Used Identifier"}, status = 400)
            if User.objects.filter(phone_number = data['phone_number']).exists():
                return JsonResponse({"message" : "Already Used Phone_number"}, status = 400)
            
            signup_user = User(
                name         = data['name'],
                birthdate    = data['birthdate'],
                identifier   = data['identifier'],
                password     = data['password'],
                gender       = data['gender'],
                phone_number = data['phone_number'],
            )
            signup_user.full_clean()
            signup_user.password = bcrypt.hashpw(signup_user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            signup_user.save()
            
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

        return JsonResponse({
                'message' : 'SUCCESS',
                'name' : data['name']
                },
                status = 200)

class SigninView(View):
    def post(self, request): 
        data = json.loads(request.body)
            
        try: 
            if User.objects.filter(identifier = data['identifier']).exists(): 
                signin_user    = User.objects.get(identifier = data['identifier'])
                input_password = data['password']
                if bcrypt.checkpw(input_password.encode('utf-8'), signin_user.password.encode('utf-8')): 
                    token = jwt.encode({'identifier' : signin_user.identifier}, SECRET_KEY, algorithm = my_settings.algorithm)
                    return JsonResponse({'token' : token.decode()}, status = 200)

                return JsonResponse({'message' : 'INVALID_PASSWORD'})
            return JsonResponse({'message' : 'INVALID_USER'}, status = 401)
        except KeyError: 
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)