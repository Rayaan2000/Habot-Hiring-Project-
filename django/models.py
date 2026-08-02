from django.db import models


class Student(models.Model):

    full_name = models.CharField(max_length=100)

    age = models.PositiveIntegerField()

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    school = models.CharField(max_length=150)

    grade = models.PositiveIntegerField()

    parent_name = models.CharField(max_length=100)

    emergency_contact = models.CharField(max_length=15)

    has_learning_difficulty = models.BooleanField(default=False)

    difficulty_type = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    consent = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name