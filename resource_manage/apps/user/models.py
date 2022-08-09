from django.db import models

# Create your models here.

import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class AccountModel(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    id = models.CharField(max_length=36, primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    password = models.CharField(_('password'), null=True, blank=True, max_length=128)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    create_time = models.DateTimeField(_('date joined'), auto_now_add=True)
    update_time = models.DateTimeField(_('date update'), auto_now=True)
    note = models.CharField(max_length=256, null=True, blank=True, verbose_name="备注")

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = '账户表'
        verbose_name_plural = verbose_name
        db_table = 't_account'
        ordering = ('-create_time',)
