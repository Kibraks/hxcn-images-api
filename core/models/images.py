"""
Image models.
"""
import os
import uuid

from django.db import models
from django.conf import settings


def get_image_file_path(instance, filename):
    """Generate file path for new recipe image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'recipe', filename)


class Image(models.Model):
    """Originally upload image."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_file_path)


class Thumbnail(models.Model):
    """Thumbnail of an image."""

    original_image = models.ForeignKey(
        'core.Image',
        on_delete=models.CASCADE,
        related_name='thumbnails',
    )
    image = models.ImageField(upload_to=get_image_file_path)
