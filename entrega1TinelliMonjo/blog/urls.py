from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from blog.views import inicio,info,experence

urlpatterns = [
    path('', inicio,name='inicio'),
    path('inicio/', inicio,name='inicio'),
    path('info/', info,name='info'),
    path('experence/', experence,name='experence'),
]