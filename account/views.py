
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

@api_view(['GET'])
def current_user(request):			# Determine the current user by their token, and return their data

    serializer = UserSerializer(request.user)
    return Response(serializer.data)