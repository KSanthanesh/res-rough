from django.db import models


class Reservation(models.Model):
    first_name = models.CharField(max_length=20)
    sur_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        db_table = "reservation"

    def __str__(self):
        return self.first_name
