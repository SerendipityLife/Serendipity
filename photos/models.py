from django.db import models
from django.dispatch import receiver
from django.conf import settings
import os


def upload_file(instance, filename):
    return(f'files/{instance.from_user.pk}/{instance.id}_{filename}')

class Photo_info(models.Model):
    period = models.IntegerField(default=0)
    send_date = models.DateTimeField()
    phone_from= models.CharField(max_length=20, null=True)
    phone_to= models.CharField(max_length=20, null=True)
    link = models.CharField(max_length=300)
    from_name=models.CharField(max_length=50)
    to_name=models.CharField(max_length=50)
    message = models.CharField(max_length=40)

class Photo(models.Model):
    photo = models.FileField(upload_to=upload_file)
    info = models.ForeignKey(Photo_info, on_delete=models.CASCADE, null=True)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    msg_flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_num = models.IntegerField()
    random_url = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        if self.id is None:
            temp_image = self.photo
            self.photo = None
            super().save(*args, **kwargs)
            self.photo = temp_image
        super().save(*args, **kwargs)

    def __str__(self):
        return(f'{self.from_user.username}-{self.photo.name}-{self.msg_flag}-{self.created_at}-{self.upload_num}')\

@receiver(models.signals.post_delete, sender=Photo)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)