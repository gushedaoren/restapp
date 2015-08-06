from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from oliver.models import Account
from oliver.response_tool import ResponseTool


class LoginView(APIView):


    def get(self, request, format=None):

        account=request.GET['account']
        password=request.GET['password']

        statusCode=0
        msg="login success!"

        try:
          a=Account.objects.get(accountName=account)
          if a.password!=password:
              statusCode=1
              msg="acount and password do not match!"

        except Account.DoesNotExit:
          statusCode=2
          msg="user not exits"



        content=ResponseTool.getResultContent(statusCode,msg)
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






        content=ResponseTool.getResultContent(statusCode,msg)




        # content = {
        #     'status': statusCode,
        #     'msg': msg,
        # }
        return Response(content)