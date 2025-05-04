from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, sdu_email, password=None, **extra_fields):
        if not sdu_email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(sdu_email)
        user = self.model(sdu_email=email, **extra_fields)
        user.set_password(password)  # Хешируем пароль
        user.is_superuser = False  # Устанавливаем для обычных пользователей is_superuser в False
        user.save(using=self._db)
        return user

    def create_superuser(self, sdu_email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)  # Для суперпользователя
        extra_fields.setdefault('is_superuser', True)  # Для суперпользователя
        return self.create_user(sdu_email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    sdu_email = models.EmailField(unique=True)
    social_gpa = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core_user_set',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='core_user_permissions_set',
        blank=True
    )

    USERNAME_FIELD = 'sdu_email'  # Для логина используется email
    EMAIL_FIELD = 'sdu_email'  # Для почты
    objects = UserManager()

    def __str__(self):
        return self.sdu_email

    @property
    def is_staff(self):
        return self.is_admin



class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='club_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='events')
    gpa_reward = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    registered_at = models.DateTimeField(auto_now_add=True)
    attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user} - {self.event}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.sdu_email}"

