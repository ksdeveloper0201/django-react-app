from django.shortcuts import render

# Create your views here.

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from .ownpermissions import ProfilePermission

# userに関するview
class UserViewSet(viewsets.ModelViewSet): # ModelViewSet何も指定しなければCRUDが全て使える。
    queryset = User.objects.all() #userオブジェクトを全て取得しquerysetに代入
    serializer_class = UserSerializer #userのシリアライザーを使うことを明示
    # permission_classes = (AllowAny,)
    permission_classes = (ProfilePermission,)

# myselfに関するview
class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user #ログインしているuser情報を指している。
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all() 
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

