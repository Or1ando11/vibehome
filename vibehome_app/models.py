from django.db import models


class Estate(models.Model):
    PROPERTY_CHOICES = (
        ('sale', 'Sale'),
        ('rent', 'Rent'),
    )
    MARKET_CHOICES = (
        ('apartment', 'Apartment'),
        ('house', 'House'),
    )
    offer_number = models.CharField(max_length=30 ,primary_key=True)
    localization = models.CharField(max_length=255)
    property_type = models.CharField(max_length=30, choices=PROPERTY_CHOICES)
    primary_market = models.CharField(max_length=30, choices=MARKET_CHOICES, null=True, blank=True)
    secondary_market = models.CharField(max_length=30, choices=MARKET_CHOICES, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    surface = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_rooms = models.PositiveIntegerField(default=0)
    description = models.TextField(default='')

    def __str__(self) -> str:
        return self.offer_number

#kontakt
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    property_type = models.CharField(max_length=255)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


#API test
class Listing(models.Model):
    description = models.TextField()
    english_description = models.TextField()
