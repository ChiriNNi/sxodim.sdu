from django.contrib import admin
from .models import User, Club, Event, EventRegistration, Notification

admin.site.register(User)
admin.site.register(Club)
admin.site.register(Event)
admin.site.register(EventRegistration)
admin.site.register(Notification)
