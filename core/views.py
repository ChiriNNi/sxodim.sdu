from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Club, Event, EventRegistration, Notification
from .serializers import UserSerializer, ClubSerializer, EventSerializer, EventRegistrationSerializer, NotificationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    # Добавляем фильтрацию по клубу с использованием DjangoFilterBackend
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)  # Используем DjangoFilterBackend
    filterset_fields = ['club']  # Фильтрация по клубу

    def get_queryset(self):
        queryset = super().get_queryset()
        club_id = self.request.query_params.get('club', None)
        if club_id:
            queryset = queryset.filter(club__id=club_id)
        return queryset

class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

