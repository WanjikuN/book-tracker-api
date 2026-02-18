from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from .models import User
from .serializers import UserSerializer, UserRegistrationSerializer


@extend_schema(
    tags=["Authentication"],
    summary="Register a new user",
    description="Create a new user account with username, email, and password",
    request=UserRegistrationSerializer,
    responses={
        201: UserSerializer,
        400: OpenApiTypes.OBJECT,
    },
    examples=[
        OpenApiExample(
            "Registration Example",
            value={
                "username": "johndoe",
                "email": "john@example.com",
                "password": "securepass123",
                "password_confirm": "securepass123",
            },
            request_only=True,
        ),
    ],
)
class RegisterView(generics.CreateAPIView):
    """
    POST api/auth/register/
    Register a new user
    """

    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]  # anyone can register

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Return user data without password
        user_serializer = UserSerializer(user)
        return Response(
            {"user": user_serializer.data, "message": "User registered successfully"},
            status=status.HTTP_201_CREATED,
        )


@extend_schema(
    tags=["Authentication"],
    summary="Get or update user profile",
    description="Retrieve or update the authenticated user profile",
    responses={
        200: UserSerializer,
        401: OpenApiTypes.OBJECT,
    },
)
class ProfileView(generics.RetrieveUpdateAPIView):
    """
    GET api/auth/profile/      - Get current user profile
    PUT api/auth/profile/      - Update current user profile
    PATCH api/auth/profile/    - Partial update current user profile
    """

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Return the current authenticated user
        return self.request.user


@extend_schema(
    tags=["Authentication"],
    summary="Logout user",
    description="Blacklist the refresh token to logout the user",
    request={
        "application/json": {
            "type": "object",
            "properties": {
                "refresh_token": {
                    "type": "string",
                    "description": "The refresh token to blacklist",
                }
            },
            "required": ["refresh_token"],
        }
    },
    responses={
        205: OpenApiTypes.OBJECT,
        400: OpenApiTypes.OBJECT,
        401: OpenApiTypes.OBJECT,
    },
    examples=[
        OpenApiExample(
            "Logout Example",
            value={"refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."},
            request_only=True,
        ),
    ],
)
class LogoutView(APIView):
    """
    POST api/auth/logout/
    Blacklist the refresh token
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response(
                    {"error": "Refresh token is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "Successfully logged out"},
                status=status.HTTP_205_RESET_CONTENT,
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
