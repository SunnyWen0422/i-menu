from django.db import models

# Create your models here.


class Dish(models.Model):
    num = models.IntegerField(primary_key=True, auto_created=True)
    name = models.TextField()
    type = models.IntegerField()
    describe = models.TextField()

    class Meta:
        db_table = "caidan"

