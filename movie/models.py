from django.db import models
from django.conf import settings
from .validators import validate_score

class Category(models.Model):
    '''Class for Categories.'''
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def is_parent(self):
        if self.parent is None:
            return True

        return False

    @property
    def get_sub_categories(self):
        '''Getting all sub_categories of a parent category'''
        return Category.objects.filter(parent=self)


class Movie(models.Model):
    '''Class for creating a movie.'''
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='movies/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_average_score(self):
        '''Getting average score of ratings of the movie.'''
        pass

class Rating(models.Model):
    '''Model for rating.'''
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='movie_ratings',
                              on_delete=models.CASCADE)
    score = models.IntegerField(default=0, validators=[validate_score])

    def __str__(self):
        return str(self.rate)
