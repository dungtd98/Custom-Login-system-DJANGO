from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, userID, password, **kwargs):
        if not userID:
            raise ValueError("userID is required")
        user = self.model(
            userID = userID,
            **kwargs
        )
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, userID, password=None, **kwargs):
        kwargs.setdefault('is_staff',False)
        kwargs.setdefault('is_admin', False)
        return self._create_user(userID, password, **kwargs)

    def create_superuser(self, userID, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_admin', True)
        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(userID, password, **kwargs)

class CustomUserModel(PermissionsMixin, AbstractBaseUser):
    userID = models.CharField(
        verbose_name="Mã nhân viên: ",
        max_length=20,
        unique=True,
        help_text=_(
            "Required, 20 characters or fewer"
        ),
        error_messages={
            "unique":_("userID already existed.")
        }
    )

    userFullname = models.CharField(
        verbose_name="Họ và tên",
        max_length=200,
        blank=False
    )

    ROLES=[
        ("EMPLOYEE", 'Nhân viên'),
        ("MANAGER",'Quản lí')
    ]
    user_role = models.CharField(
        verbose_name="Chức vụ",
        max_length=30,
        choices=ROLES,
        default='EMPLOYEE'
    )

    is_staff = models.BooleanField(
        _("staff_status"),
        default=False,
        help_text=_("")
        )