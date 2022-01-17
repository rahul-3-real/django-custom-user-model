from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('movies/', include('movies.urls', namespace='movies')),
]

admin.site.site_header = 'Custom User Model'
admin.site.index_title = 'Manage Site Administration'
