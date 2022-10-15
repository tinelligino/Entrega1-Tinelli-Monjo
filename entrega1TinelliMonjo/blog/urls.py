from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from blog.views import inicio, info, experence, contact, historia, buscar

urlpatterns = [
    path("", inicio, name="inicio"),
    path("inicio/", inicio, name="inicio"),
    path("info/", info, name="info"),
    path("experence/", experence, name="experence"),
    path("contact/", contact, name="contact"),
    path("historia/", historia, name="historia"),
    path("buscar/", buscar, name="buscar"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)