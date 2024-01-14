from django.contrib.auth.models import UserManager


class CustomUSerManager(UserManager):
    '''Custom manager for user model with phone number as USERNAME field.'''

    def create_user(self, phone_number, password, **extra_fields):
        '''Function for creating a normal user with phone number field.'''

        if not phone_number:
            raise ValueError('Phone number must be set.')

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        '''Function for creating a super user.'''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(
            phone_number=phone_number,
            password=password,
            **extra_fields,
            )
