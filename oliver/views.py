from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
import logging

class LoginView(APIView):


    def get(self, request, format=None):

        account=request.GET['account']
		print("account"+account)
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth),
        }
        return Response(content)