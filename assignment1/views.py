from django.http import JsonResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def send_massages(request):
    # request.GET
    return Response({'massage': 'susses'})
