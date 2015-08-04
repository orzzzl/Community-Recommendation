from django.db import models

# Create your models here.
class score (models.Model):
    zipCode = models.CharField(max_length=10, default="#####")
    money = models.IntegerField(default="0")
    school = models.FloatField(default="0.0")
    eating = models.FloatField(default="0.0")
    shopping = models.FloatField(default="0.0")
    security = models.FloatField(default="0.0")
    health = models.FloatField(default="0.0")
    transportation = models.FloatField(default="0.0")
    clinicNumber = models.IntegerField(default="0")
    preschoolNumber = models.IntegerField(default="0")

    def __unicode__(self):
        return unicode(self.zipCode)

