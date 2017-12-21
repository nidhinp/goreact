from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator


class MemberManager(BaseUserManager):
    def create_user(self, email, phone, password=None):
        if not email:
            raise ValueError('Users must have an email')

        user = self.model(
            email=self.normalize_email(email), phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, phone, password=None):
        user = self.create_user(
            email=email, phone=phone, password=password
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Member(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phoneRegex = RegexValidator(
        regex=r'^\+[\d]+$|^[\d]+$', message="Only + and digits allowed"
    )
    phone = models.CharField(max_length=20, validators=[phoneRegex])
    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('phone',)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email or u''

    class Meta:
        ordering = ('-id',)
