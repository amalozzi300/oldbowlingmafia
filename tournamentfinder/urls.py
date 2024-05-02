from django.urls import path

from tournamentfinder import views

urlpatterns = [
    # BowlingCenter
    path('bowling-centers', views.BowlingCenterList.as_view(), name='list_centers'),
    path('bowling-centers/create', views.BowlingCenterCreate.as_view(), name='create_center'),
    path('bowling-centers/update/<pk>', views.BowlingCenterUpdate.as_view(), name='update_center'),
    path('bowling-centers/delete/<pk>', views.BowlingCenterDelete.as_view(), name='delete_center'),
    # TournamentDirector
    path('tournament-directors', views.TournamentDirectorList.as_view(), name='list_directors'),
    path('tournament-directors/create', views.TournamentDirectorCreate.as_view(), name='create_director'),
    path('tournament-directors/update/<pk>', views.TournamentDirectorUpdate.as_view(), name='update_director'),
    path('tournament-director/delete/<pk>', views.TournamentDirectorDelete.as_view(), name='delete_director'),
    # Tournament
    path('tournaments', views.TournamentList.as_view(), name='list_tournaments'),
    path('tournaments/create', views.TournamentCreate.as_view(), name='create_tournament'),
    path('tournaments/update/<pk>', views.TournamentUpdate.as_view(), name='update_tournament'),
    path('tournaments/delete/<pk>', views.TournamentDelete.as_view(), name='delete_tournament'),
]