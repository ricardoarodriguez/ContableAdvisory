Skip to content
Product
Solutions
Open Source
Pricing
Search
Sign in
Sign up
veryacademy
/
YT-Django-DRF-Simple-Blog-Series-JWT-Part-3
Public
Code
Issues
1
Pull requests
Actions
Projects
Security
Insights
YT-Django-DRF-Simple-Blog-Series-JWT-Part-3/django/users/views.py /
@veryacademy
veryacademy nc
Latest commit a09743a on 15 Sep 2020
 History
 0 contributors
34 lines (28 sloc)  1.21 KB

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
