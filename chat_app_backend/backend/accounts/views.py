from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from accounts.tokenauthentication import JWTAuthentication
from .serializers import UserSerializer, LoginSerializer

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user_data = serializer.validated_data
        token = JWTAuthentication.generate_token(payload={'id': user_data['id'], 'email': user_data['email']})
        return Response({
            "message": 'Login Successfull',
            "token": token,
            "user": serializer.data
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
