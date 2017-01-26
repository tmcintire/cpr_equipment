from django.db import models


class Drivers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return "%s %s" %(self.first_name, self.last_name)


class Type(models.Model):
    type = models.CharField(max_length=100, verbose_name="Type", unique=True)

    def __unicode__(self):
        return self.type


class Department(models.Model):
    department = models.CharField(max_length=100, verbose_name="Department", unique=True)

    def __unicode__(self):
        return self.department


class Equipment(models.Model):
    number = models.CharField(max_length=100, unique=True)
    department = models.ForeignKey(Department, null=True, blank=True)
    in_service = models.DateField(null=True, blank=True, verbose_name="In Service Date")
    type = models.ForeignKey(Type, null=True)
    name = models.CharField(max_length=100)
    vin = models.CharField(max_length=100, blank=True, null=True)
    tag = models.CharField(max_length=100, blank=True, null=True)
    driver = models.ForeignKey(Drivers, null=True, blank=True)

    def total_cost(self):
        return sum(self.service_set.all().values_list('cost', flat=True))

    def __unicode__(self):
        return self.number


class Service(models.Model):
    equipment_id = models.ForeignKey(Equipment, verbose_name="Equipment")
    service_date = models.DateField(verbose_name="Service Date")
    summary = models.CharField(max_length=100)
    notes = models.TextField()
    cost = models.DecimalField(max_digits=15, decimal_places=2)
