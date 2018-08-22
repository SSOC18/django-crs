from django.db import models
import factory
import factory.django
# Create your models here.

class crs(models.Model):
    accounts=models.CharField(max_length=64)
    accountbalances=models.CharField(max_length=64)
    names=models.CharField(max_length=64)

    def __str__(self):
        return self.names


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = crs
    
    accounts = factory.Faker('iban')
    accountbalances = factory.Faker('ean8')
    names = factory.Faker('name')

