from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    category = models.ForeignKey(Category)
    # category = models.ManyToManyField(Category)
    topic = models.CharField(max_length=30)
    note = models.TextField()
    date_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.topic
