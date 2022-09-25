
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import Taskserializer,Attendanceserizer
from .models import Task,Attendence

# Create your views here.
@api_view(['POST'])
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return Response('you are logged in succesfully')
        ...
    else:
        return Response('login failed')
        ...

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    logout(request)
    return Response('successfully logged out')

class Taskviewset(viewsets.ModelViewSet):
    serializer_class = Taskserializer
    queryset = Task.objects.all()

    def create(self,request,*args,**kwargs):
        if request.user.userprofile.last().role =='supervisor':
            serializer = Taskserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Task has been assigned successfully")
            else:
                return Response("invalid data")
        else:
            return Response("you cannot assign task")

class AttendenceViewset(viewsets.ModelViewSet):
    serializer_class = Attendanceserizer
    queryset = Attendence.objects.all()
    permission_classes = [IsAuthenticated,]

    def create(self,request,*args,**kwargs):
        if request.user.userprofile.last().role =='intern':
            Attendence.objects.create(user=request.user,is_present=True)
            return Response("Success")
        else:
            return Response("invalid user, user must be intern")
            