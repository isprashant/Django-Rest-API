from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from datetime import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
docs_storage = FileSystemStorage(location=settings.DOCS_STORAGE_ROOT)


def driving_files():
    a = str(datetime.now().strftime("%H:%M:%S"))
    return 'uploads/driving_licence/' + 'DL' + '-'.join(a.split(':'))


def pancard_files():
    a = str(datetime.now().strftime("%H:%M:%S"))

    return 'uploads/pancard/' + 'pancard' + '-'.join(a.split(':'))


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=25, default='')
    phone_regex = RegexValidator(regex=r'^\d{10}$', message= \
        "Phone number must be of 10 digits")
    mobile = models.CharField(validators=[phone_regex], max_length=10, blank=True, default='')
    driving_licence = models.FileField(upload_to=driving_files(), storage=docs_storage)
    pancard = models.FileField(upload_to=pancard_files(), storage=docs_storage)
    is_driving_licence_verified = models.BooleanField(default=False)
    is_pancard_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def is_dl_verified(self):
        if self.is_driving_licence_verified:
            return True
        return False

    is_dl_verified.boolean = True

    def is_pc_verified(self):
        if self.is_pancard_verified:
            return True
        return False

    is_pc_verified.boolean = True


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
