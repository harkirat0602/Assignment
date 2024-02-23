from django.db import models

# Create your models here.

class Organization(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=20)


class Item(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    type=models.CharField(max_length=20)
    description = models.CharField(max_length=60)

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    # organization_id = organization.id
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # item_id = item.id
    zone= models.CharField(max_length=20)
    base_distance_in_km= 5
    km_price=models.IntegerField()
    fix_price=10