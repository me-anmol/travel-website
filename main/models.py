from django.db import models


# Create your models here.
class destinations(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    offer = models.BooleanField(default=False)
    img = models.ImageField(upload_to='pics')
    per_day_cost = models.FloatField()
    no_of_visits = models.IntegerField()
    type_of_vacation = [
        ('Beach', 'Beach'),
        ('HillStation', 'HillStation'),
        ('safari', 'safari'),
        ('city', 'city'),
        ('International', 'International')
    ]
    type = models.CharField(max_length=100, choices=type_of_vacation)


class messages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)
    subject = models.CharField(max_length=100)
    text = models.TextField()


class news(models.Model):
    date = models.DateField()
    subject = models.CharField(max_length=200)
    desc = models.TextField()
    img = models.ImageField(upload_to='news')
    cat = [
        ('Travel', 'Travel'),
        ('Organization', 'Organization'),
        ('uncategorized', 'uncategorized'),
    ]
    category = models.CharField(max_length=100, choices=cat)


class subscribers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


