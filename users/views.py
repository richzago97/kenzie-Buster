from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import ISAuthenticatedUser
from .serializers import UserSerializer
from .models import User
from django.shortcuts import get_object_or_404
import ipdb


class RegisterView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    ...


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, ISAuthenticatedUser]

    def get(self, req: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(req, user)
        serializer = UserSerializer(user)

        return Response(serializer.data)
