from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lesson(models.Model):
    number = models.IntegerField(primary_key=True, default=1)
    name = models.CharField(max_length=30, default="Not set")

    def __str__(self):
        return self.name


class Badge(models.Model):
    name = models.CharField(max_length=30, default="Not set")
    icon = models.ImageField(upload_to="badges")
    lesson_requirement = models.IntegerField(default=1)


class ClientProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_lesson = models.CharField(max_length=30, blank=True)
    completed_lessons = models.ManyToManyField(Lesson)
    badges_earned = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
