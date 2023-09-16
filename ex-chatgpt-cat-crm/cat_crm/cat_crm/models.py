from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    owner = models.ForeignKey("Owner", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    purpose = models.CharField(max_length=255)

    def __str__(self):
        return f"Appointment for {self.cat.name} on {self.date} at {self.time}"
