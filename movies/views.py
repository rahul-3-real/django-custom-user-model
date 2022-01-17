from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Commercial, Film
from .forms import MovieSelectForm, FilmModelForm, CommercialModelForm

# Create your views here.


class MovieSelectFormView(LoginRequiredMixin, FormView):
    form_class = MovieSelectForm
    template_name = 'movies/index.html'
    success_url = reverse_lazy('movies:add-movie')

    def post(self, *args, **kwargs):
        self.request.session['movie'] = self.request.POST.get('movie').title()
        return super().post(*args, **kwargs)


class AddMovieFormView(LoginRequiredMixin, FormView):
    template_name = 'movies/add.html'
    success_url = reverse_lazy('index')

    def get_form_class(self, *args, **kwargs):
        movie = self.request.session.get('movie')
        if movie == 'Film':
            return FilmModelForm
        else:
            return CommercialModelForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
