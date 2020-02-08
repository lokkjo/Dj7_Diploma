from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


# from goods.models import Item

class UserManager(BaseUserManager):
    """
    Define a model manager for User model with no username field
    from www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        База для создания и сохранения Пользователя (User)
        принимает почту и пароль
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Создаёт и сохраняет простого пользователя
        принимает почту и пароль
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Создаёт и сохраняет пользователя-администратора (superuser)
        принимает почту и пароль
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Модель пользователя (User)
    """
    username = None
    email = models.EmailField(_('почта'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
