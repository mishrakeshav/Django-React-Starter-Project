from django.shortcuts import render
from rest_framework import generics, serializers
import django_filters.rest_framework
from rest_framework import filters
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import permissions
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


from users.models import Profile


from .serializers import UserSerializer , ProfileSerializer


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user 

class UserDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, format=None):
        user = self.get_object(request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data) 
    
    def put(self, request,format=None):
        user = self.get_object(request.user.id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,format=None):
        user = self.get_object(request.user.id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = ProfileSerializer
