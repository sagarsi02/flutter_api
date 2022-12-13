from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User, auth
import json
from django.http import HttpResponse


class createuser(APIView):

    def post(request, *args, **kwargs):
        try:
            body = request.request.data

            if body.get('f_name', ''):
                f_name = body['f_name']
                l_name = body['l_name']
                username = body['username']
                email = body['email']
                password = body['password']
                c_password = body['c_password']
            

                if password == c_password:
                    if User.objects.filter(email=email).exists():
                        return HttpResponse('Already Register')
                    elif User.objects.filter(username=username).exists():
                        return HttpResponse('username is already taken')
                    else:
                        usr = User.objects.create_user(first_name=f_name, last_name=l_name, username=username, email=email, password=password)
                        usr.save();
                        return HttpResponse('Successfully Registered')
                else:
                    return HttpResponse('Password does\'t match')

        except:
            return HttpResponse('Invalid Credentials')



class login(APIView):
    def post(request, *args, **kwargs):

        try:
            body = request.request.data

            if body.get('username', ''):
                username = body['username']
                password = body['password']
                
                user = auth.authenticate(username=username, password=password)
                
                if user is not None:
                    auth.login(request.request, user)
                    # return render(request, 'home.html')
                    return HttpResponse('Logged in')
                else:
                    return HttpResponse('User is not exist')
        except:
            return HttpResponse('Invalid Credentials')
