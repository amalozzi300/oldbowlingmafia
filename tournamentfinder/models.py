from django.db import models
from django.contrib.auth.models import User

import string as s
from localflavor.us.models import USStateField, USZipCodeField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class BowlingCenter(models.Model):
    center_name = models.CharField(max_length=64)
    street_address = models.CharField(max_length=128, verbose_name='address')
    city = models.CharField(max_length=64)
    state = USStateField()
    zip_code = USZipCodeField(max_length=5)
    phone_number = PhoneNumberField()
    website = models.URLField(max_length=256, blank=True)

    def __str__(self):
        return f'{s.capwords(self.center_name, sep=" ")} - {s.capwords(self.city, sep=" ")}, {str(self.state)}'

    class Meta:
        verbose_name = 'Bowling Center'
        ordering = ['state', 'center_name']

class TournamentDirector(models.Model):
    director_user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_address = models.EmailField(max_length=128)
    phone_number = PhoneNumberField()
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return f'{s.capwords(self.first_name)} {s.capwords(self.last_name)}'

    class Meta:
        verbose_name = 'Tournament Director'
        ordering = ['first_name', 'last_name']

class Tournament(models.Model):
    tournament_name = models.CharField(max_length=128)
    start_time = models.DateTimeField()
    bowling_center = models.ForeignKey(BowlingCenter, on_delete=models.CASCADE)
    tournament_director = models.ForeignKey(TournamentDirector, on_delete=models.CASCADE)
    flyer = models.FileField(upload_to='tournament_flyers', blank=True)
    website = models.URLField(max_length=256, blank=True)

    def __str__(self):
        return s.capwords(self.tournament_name)
    
    class Meta:
        ordering = ['start_time']