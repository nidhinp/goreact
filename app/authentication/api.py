from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import authenticate

from .serializers import MemberSerializer
from .models import Member


class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("email", None)
        password = request.data.get("password", None)

        member = authenticate(email=username, password=password)

        if member is not None:
            if member.is_active:
                serializer = MemberSerializer(member)
                return Response(serializer.data)
            else:
                return Response(
                    {"error": "This account is not activated yet."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {"error": "Email password combination invalid."},
                status=status.HTTP_401_UNAUTHORIZED
            )
