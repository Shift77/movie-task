from django.core.exceptions import ValidationError


def validate_score(value):
    '''Validating score of rating model.'''
    if value < 0 or value > 5:
        raise ValidationError('Score must not be less tan 0 and more than 5.')

    return value
