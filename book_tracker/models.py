# book_tracker/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Lean for now but ready for expansion.
    """

    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", null=True, blank=True
    )
    reading_goal = models.PositiveIntegerField(
        null=True, blank=True, help_text="Number of books user aims to read per year"
    )
    is_private = models.BooleanField(
        default=False, help_text="Whether the user's reading list is private"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"
        ordering = ["-date_joined"]

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def has_reading_goal(self):
        return self.reading_goal is not None
