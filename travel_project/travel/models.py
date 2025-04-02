
from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='destination_images/')
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class TourPackage(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField(help_text="Duration in days")
    departure_date = models.DateField()
    return_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.destination.name} - {self.duration} days"

class Booking(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.EmailField()
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    number_of_people = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking by {self.user_name} for {self.tour_package.destination.name}"
