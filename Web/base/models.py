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
        kwargs.setdefault('is_superuser', False)
        return self._create_user(userID, password, **kwargs)

    def create_superuser(self, userID, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
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
        help_text=(
            "Required, 20 characters or fewer"
        ),
        error_messages={
            "unique":("userID already existed.")
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
    userRole = models.CharField(
        verbose_name="Chức vụ",
        max_length=30,
        choices=ROLES,
        default='EMPLOYEE'
    )

    is_staff = models.BooleanField(
        ("staff_status"),
        default=False,
        help_text=("Designate whether this user can log into admin site "),
        )
    
    is_active = models.BooleanField(
        ("active"),
        default= True,
        help_text=(
            "Designate whether this user should be treated as active."
            "Unselected this instead of deleted account"
        )
    )

    is_superuser = models.BooleanField(
        ("superuser status"),
        default=False,
        help_text=(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )

    ABSENT_STATUS = [
        ("ONDUTY",'bình thường'),
        ("ANUAL_LEAVE", 'phép năm'),
        ("NOREASON_LEAVE",'nghỉ tự do'),
        ("SICK_LEAVE","phép bệnh"),
        ("PRIVATE_LEAVE","Phép riêng")
    ]
    workingStatus = models.CharField(
        verbose_name="Điểm danh",
        max_length=30,
        choices=ABSENT_STATUS,
        default="ONDUTY"
    )

    objects = CustomUserManager()
    USERNAME_FIELD = "userID"
    REQUIRED_FIELDS = ["userFullname"]
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def __str__(self) -> str:
        return self.userFullname

