from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework.permissions import *
from .serializers import *
from .models import *
from .permissions import *

class UserRegisterAPIView(APIView):
    @swagger_auto_schema(
        request_body=UserRegisterSerializer
    )
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(role='Regular')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailsAPIView(APIView):
    permission_classes = [IsRegularUser]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsRegularUser]

    def destroy(self, request):
        user = self.get_object()
        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsRegularUser]

    def update(self, request):
        user = self.get_object()
        if user.role == 'Regular':
            serializer = self.get_serializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)