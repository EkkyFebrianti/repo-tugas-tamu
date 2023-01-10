from django.db import models

# Create your models here.


class ItemsModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    price = models.IntegerField()

    class Meta:
        ordering = ['name']

    def _str_(self):
        return f"{self.name}:{self.price}"
        # return self.name