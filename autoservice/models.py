from django.db import models

# Create your models here.


class Autoservice(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "autoservice"

    def __str__(self):
        return '%s' % (self.name)


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)

    class Meta:
        db_table = "client"


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "service"

    def __str__(self):
        return '%s' % (self.name)


class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    cost = models.IntegerField(default=0)
    text = models.CharField(max_length=500)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    autoservice = models.ForeignKey(Autoservice, on_delete=models.CASCADE)

    class Meta:
        db_table = "offer"


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        db_table = "request"
