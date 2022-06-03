from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from .forms import UserCreationForm, UserChangeForm


from django.contrib.auth import get_user_model
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

UserModel = get_user_model()

admin.site.unregister([ Group,])
admin.site.register(UserModel)

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    fieldsets = (
        ('Account',{'fields':('userID','password')}),
        ('Personal Infor',{'fields': ('userFullname','userRole')}),
        ('Onduty Status',{'fields':('workingStatus')}),
        ('Permissions',{'fields':(
            "is_active",
            "is_staff",
            "is_superuser"
        )})
    )

    add_fieldsets = (
        ('Account login infor',{'fields':(
            "userID",
            'userFullname',
            'password1',
            'password2'
        )})
    )
    search_fields =['userID', 'userFullname']
    ordering = ['id','userID','userFullname']
    