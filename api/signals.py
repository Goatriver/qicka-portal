from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Every time user is created, add api token for it


def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


post_save.connect(create_auth_token, sender=settings.AUTH_USER_MODEL)


