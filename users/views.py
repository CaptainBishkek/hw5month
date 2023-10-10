from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import ConfirmationCode
from . import serializers

class UserRegistrationAPIView(CreateAPIView):
    serializer_class = serializers.UserRegistrationSerializer

class ConfirmUserAPIView(APIView):
    def post(self, request):
        code = request.data.get('code')
        try:
            confirmation_code = ConfirmationCode.objects.get(code=code)
            if confirmation_code.is_expired():
                return Response(data={"error": "Confirmation code has expired. Please register again."}, status=status.HTTP_400_BAD_REQUEST)
            user = confirmation_code.user
            user.is_active = True
            user.save()
            return Response(data={"message": "User successfully confirmed."}, status=status.HTTP_200_OK)
        except ConfirmationCode.DoesNotExist:
            return Response(data={"error": "Invalid confirmation code."}, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error': 'Invalid credentials'})
