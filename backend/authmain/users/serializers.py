from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer  # type: ignore


User = get_user_model()


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
