from django.contrib.auth import get_user_model

from rest_framework.viewsets import ModelViewSet

from profiles.serializers import UserSerializer


USER = get_user_model()

class UserViewSet(ModelViewSet):
    """
    Viewset to create, edit, update and list users.
    """

    queryset = USER.objects.all()
    serializer_class = UserSerializer




