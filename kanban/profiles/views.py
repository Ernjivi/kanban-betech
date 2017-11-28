from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from profiles.serializers import UserSerializer, ChangePasswordSerializer


USER = get_user_model()

class UserViewSet(ModelViewSet):
    """
    Viewset to create, edit, update and list users.
    """

    queryset = USER.objects.all()
    serializer_class = UserSerializer


    @detail_route(methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['new_password'])
            user.save()
            return Response({'status': 'password set'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


