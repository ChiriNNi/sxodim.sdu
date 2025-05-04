from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Club, Event, EventRegistration, Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'sdu_email', 'social_gpa', 'is_active']

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'description']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'club', 'gpa_reward']

class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = ['id', 'user', 'event', 'registered_at', 'attended']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'created_at', 'is_read']


class CustomAuthTokenSerializer(serializers.Serializer):
    username = serializers.EmailField()  # Используем email как имя пользователя
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('username')
        password = data.get('password')

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError('Невозможно войти с предоставленными учетными данными.')

        return {'user': user}