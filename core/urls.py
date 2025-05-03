from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ClubViewSet, EventViewSet, EventRegistrationViewSet, NotificationViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clubs', ClubViewSet)
router.register(r'events', EventViewSet)
router.register(r'registrations', EventRegistrationViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
