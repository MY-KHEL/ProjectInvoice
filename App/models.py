from django.db import models

# Create your models here.
class AddStock(models.Model):
    first_name = models.CharField(("FirstName"), max_length=50)
    last_name = models.CharField(("Last name"), max_length=50)
    quantity = models.IntegerField(("Quantity"))
