from rest_framework import serializers
from user_profile.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('user', 'about','city','mobile','driving_licence','pancard','is_driving_licence_verified',
        'is_pancard_verified')

