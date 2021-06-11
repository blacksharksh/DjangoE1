from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *

# urls
urlpatterns = [
    path("", home, name="home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIAROOT)
