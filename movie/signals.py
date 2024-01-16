from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .tasks import send_email_on_movie_save
from .models import Movie
from django.dispatch import receiver


@receiver(post_save, sender=Movie)
def send_email_to_all_users(sender, **kwargs):
    send_email_on_movie_save.delay()
