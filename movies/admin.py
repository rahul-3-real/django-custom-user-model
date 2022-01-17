from django.contrib import admin
from .models import Commercial, Film
from actors.models import Actor

# Register your models here.


class FilmModelAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['actors'].queryset = Actor.objects.filter(
            is_star=True)
        return super().render_change_form(request, context, *args, **kwargs)


class CommercialModelAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['actors'].queryset = Actor.objects.filter(
            is_star=False)
        return super().render_change_form(request, context, *args, **kwargs)


admin.site.register(Film, FilmModelAdmin)
admin.site.register(Commercial, CommercialModelAdmin)
