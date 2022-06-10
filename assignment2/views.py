from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.views import APIView


class RankUser(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class FirstView(APIView):
    # permission_classes = [AllowAny]

    permission_classes = [RankUser]

    def get(self, request, format=None):
        return HttpResponse(f"<h1>성공<br>{request.user}님 안녕하세요</h1>")
