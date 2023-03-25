from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from pyjm.permissions import SuperCheck
from .models import UserData

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class AdminRegisterView(APIView):
    permission_classes = [SuperCheck]
    def post(self, request):
        serialized_data = UserSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        user = UserData(email=serialized_data['email'].value,
                        name=serialized_data['name'].value,
                        is_staff=True
                        )
        user.set_password(serialized_data['password'].value)
        user.save()
        return Response("OK")



