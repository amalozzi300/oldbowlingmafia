from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from bowlingmafia.utils import get_login_status

from tournamentfinder.forms import BowlingCenterForm, TournamentDirectorForm, TournamentForm
from tournamentfinder.models import BowlingCenter, TournamentDirector, Tournament

# Create your views here.
class BowlingCenterList(ListView):
    model = BowlingCenter
    context_object_name = 'bowling_centers'
    template_name = 'tournamentfinder/list_centers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_in'] = get_login_status(self.request)
        return context

class BowlingCenterCreate(LoginRequiredMixin, CreateView):
    model = BowlingCenter
    form_class = BowlingCenterForm
    template_name = 'tournamentfinder/generic_model_create.html'
    success_url = reverse_lazy('list_centers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Bowling Center'
        return context

class BowlingCenterUpdate(LoginRequiredMixin, UpdateView):
    model = BowlingCenter
    form_class = BowlingCenterForm
    context_object_name = 'object'
    template_name = 'tournamentfinder/generic_model_update.html'
    success_url = reverse_lazy('list_centers')

class BowlingCenterDelete(LoginRequiredMixin, DeleteView):
    model = BowlingCenter
    context_object_name = 'object'
    template_name = 'tournamentfinder/generic_model_delete.html'
    success_url = reverse_lazy('list_centers')

class TournamentDirectorList(ListView):
    model = TournamentDirector
    context_object_name = 'tournament_directors'
    template_name = 'tournamentfinder/list_directors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_in'] = get_login_status(self.request)
        return context

class TournamentDirectorCreate(LoginRequiredMixin, CreateView):
    model = TournamentDirector
    form_class = TournamentDirectorForm
    template_name = 'tournamentfinder/generic_model_create.html'
    success_url = reverse_lazy('list_directors')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Tournament Director'
        return context

class TournamentDirectorUpdate(LoginRequiredMixin, UpdateView):
    model = TournamentDirector
    form_class = TournamentDirectorForm
    context_object_name = 'object'
    template_name = 'tournamentfinder/generic_model_update.html'
    success_url = reverse_lazy('list_directors')

class TournamentDirectorDelete(LoginRequiredMixin, DeleteView):
    model = TournamentDirector
    context_object_name = 'object'
    template_name = 'tournamentfinder/generic_model_delete.html'
    success_url = reverse_lazy('list_directors')

class TournamentList(ListView):
    model = Tournament
    context_object_name = 'tournaments'
    template_name = 'tournamentfinder/list_tournaments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logged_in'] = get_login_status(self.request)
        return context

class TournamentCreate(LoginRequiredMixin, CreateView):
    model = Tournament
    form_class = TournamentForm
    template_name = 'tournamentfinder/generic_model_create.html'
    success_url = reverse_lazy('list_tournaments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Tournament'
        return context

class TournamentUpdate(LoginRequiredMixin, UpdateView):
    model = Tournament
    form_class = TournamentForm
    context_object_name = 'object'
    template_name = 'tournamentfinder/generic_model_update.html'
    success_url = reverse_lazy('list_tournaments')

class TournamentDelete(LoginRequiredMixin, DeleteView):
    model = Tournament
    context_object_name = 'object'
    template_name = 'tournament_finder/generic_model_delete.html'
    success_url = reverse_lazy('list_tournaments')