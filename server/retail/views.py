from rest_framework import viewsets
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from retail.models import Chain, Store, Employee
from retail.serializers import ChainSerializer, StoreSerializer,EmployeeSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
import logging
import json


logger = logging.getLogger(__name__)


class ChainViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer


class StoreViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Store objects """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# @api_view(['GET', 'POST'])
class UserLoginResource(APIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        logger.error(request.data.get('username'))
        user = User.objects.get(username=request.data.get('username'))

        if not user:
            return Response({"Reason": "No user profile associated with this account"},
                            status=status.HTTP_403_FORBIDDEN)
        if user.password == request.data.get('password'):
        # user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        # if user is not None:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Reason": "Password is incorrect"},
                            status=status.HTTP_403_FORBIDDEN)
        # return Response(status=status.HTTP_200_OK)