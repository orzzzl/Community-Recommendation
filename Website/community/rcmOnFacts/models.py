from django.db import models

# Create your models here.
class cityData (models.Model):
    zipCode = models.CharField(max_length=10, default="#####")
    malePercentage = models.FloatField(default="0.0")
    femalePercentage = models.FloatField(default="0.0")
    neverMarried = models.FloatField(default="0.0")
    nowMarried = models.FloatField(default="0.0")
    seperated = models.FloatField(default="0.0")
    divorced = models.FloatField(default="0.0")
    widowed = models.FloatField(default="0.0")
    white = models.FloatField(default="0.0")
    black = models.FloatField(default="0.0")
    americanIndian = models.FloatField(default="0.0")
    asian = models.FloatField(default="0.0")
    hispanic = models.FloatField(default="0.0")
    hawaiian = models.FloatField(default="0.0")
    twoOrMore = models.FloatField(default="0.0")
    otherRace = models.FloatField(default="0.0")
    gay = models.FloatField(default="0.0")
    lesbian = models.FloatField(default="0.0")
    rent = models.FloatField(default="0.0")
    buy = models.FloatField(default="0.0")
    noEducation = models.FloatField(default="0.0")
    highSchool = models.FloatField(default="0.0")
    bachelor = models.FloatField(default="0.0")
    master = models.FloatField(default="0.0")
    def __unicode__(self):
        return unicode(self.zipCode)

