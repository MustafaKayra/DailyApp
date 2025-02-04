from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """ Normal bir kullanıcı oluşturur """
        if not username:
            raise ValueError(_('The Username field must be set'))
        if not email:
            raise ValueError(_('The Email field must be set'))
        
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        extra_fields.setdefault('is_active', True)

        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Şifreyi güvenli bir şekilde hashler
        user.save(using=self._db)
        return user


    def create_superuser(self, username, email, password=None, **extra_fields):
        """ Superuser oluşturur """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, null=True, blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email", "password"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    #def get_userupdate_url(self):
        #return reverse("userupdate", kwargs={"pk": self.pk})
    
    #def get_userdetail_url(self):
        #return reverse("userdetail", kwargs={"pk": self.pk})
