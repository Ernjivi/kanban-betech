from rest_framework import serializers

from django.contrib.auth import get_user_model

from profiles.models import Profile


USER = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for profile model.
    """

    class Meta:
        model = Profile
        fields = ['id', 'gender', 'birth_date', 'profile_image']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user model.
    """

    profile = ProfileSerializer(many=False, required=False)

    class Meta:
        model = USER
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
            'profile', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, email):
        if self.instance and email != self.instance.email:
            exists = USER.objects.filter(email=email).exists()
            if exists:
                raise serializers.ValidationError(
                    'The email allready exists, try recovering your password.')
        return email

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = super(UserSerializer, self).create(validated_data)
        if profile_data:
            self.update_or_create_profile(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        if profile_data:
            self.update_or_create_profile(instance, **profile_data)
        return super(UserSerializer, self).update(instance, validated_data)

    def update_or_create_profile(self, user, **kwargs):
        Profile.objects.update_or_create(user=user, **kwargs)

