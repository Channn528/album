from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    objects = models.Manager()
    image = models.ImageField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )    
    like_user_set = models.ManyToManyField(
        User,
        null=True,
        blank=True,
        related_name='like_user_set',
        through='Like',
    )    
    created_at = models.DataTimeField(auto_now_add=True)
    updated_at = models.DataTimeField(auto_now=True)
    
class Like(models.Model):

    post = models.ForeignKey(
        "Post",
    )

    user = models.ForeignKey(
        User,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )    