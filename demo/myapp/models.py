from django.db import models



class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email =models.CharField(max_length=200, default="")
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_people = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name