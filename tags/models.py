from django.db import models
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='tags',
        blank=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
