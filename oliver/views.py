from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
import logging
from oliver.models import Account


class LoginView(APIView):


    def get(self, request, format=None):

        account=request.GET['account']
        password=request.GET['password']

        statusCode=0
        msg="login success!"



        content = {
            'status': statusCode,
            'msg': msg,
        }
        return Response(content)



class RegisterView(APIView):


    def get(self, request, format=None):

        account=request.GET['account']
        password=request.GET['password']
        statusCode=0
        msg="register success!"

        try:

            a=Account.objects.get(accountName=account)

            statusCode=1
            msg="user exits!"

        except ObjectDoesNotExist:

            a=Account()
            a.accountName=account
            a.password=password
            a.save()











        content = {
            'status': statusCode,
            'msg': msg,
        }
        return Response(content)