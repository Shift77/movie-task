from django.contrib.auth import get_user_model
from .models import Movie
from celery import shared_task

@shared_task
def send_email_on_movie_save():
    all_users = get_user_model().objects.all()

    # getting all user emails.
    all_emails = list()
    for user in all_users:
        all_emails.append(user.email)

    # getting the last movie created.
    last_movie = Movie.objects.latest('id')

    # Now that we have the all emails and the last move that created
    # we can process the movie and send an email for each in order to
    # notify them.
