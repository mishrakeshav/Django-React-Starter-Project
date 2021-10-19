from django.shortcuts import render
from rest_framework import generics, serializers
import django_filters.rest_framework
from rest_framework import filters
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import permissions

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

class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = ProfileSerializer
