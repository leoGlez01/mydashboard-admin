from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('djadmin/', admin.site.urls),
    path('', include('board.urls')),
]
