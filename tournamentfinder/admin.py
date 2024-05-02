from django.contrib import admin

from tournamentfinder.models import BowlingCenter, TournamentDirector, Tournament

# Register your models here.
admin.site.register(BowlingCenter)
admin.site.register(TournamentDirector)
admin.site.register(Tournament)