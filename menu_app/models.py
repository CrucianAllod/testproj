from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name