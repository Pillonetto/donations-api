from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title

class StoreItem(models.Model):
    name = models.CharField(max_length=120, primary_key=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    provider = models.IntegerField(default=-1)

    def __str__(self):
        return self.name

class RedeemedStoreItem(models.Model):
    item = models.ForeignKey(StoreItem, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.name
