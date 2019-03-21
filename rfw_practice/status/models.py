from django.conf import settings
from django.db import models

# 照理說model不用建的那麼複雜

def upload_status_image(instance, filename) :
    return "update/{user}/{filename}".format(user=instance.user, filename=filename)

class StatusQuerySet(models.QuerySet):
    pass

class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)
class Status( models.Model ):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=False )
    content = models.TextField()
    image = models.ImageField(upload_to=upload_status_image, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = StatusManager()
    def __str__(self):
        return str(self.content)[:50]

    class Meta:
        verbose_name = 'StatusHHHH post' #admin最裡面的介面
        verbose_name_plural = 'Statuss post' #admin最外面的介面


    # 外定義model
    @property
    def owner(self):
        return self.user