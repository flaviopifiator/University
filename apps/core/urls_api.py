from django.urls import path
from rest_framework import routers

from apps.universidad.api.urls import urlpatterns as url_universidad
from apps.facultad.api.urls import urlpatterns as url_facultad
from apps.materia.api.urls import urlpatterns as url_materia


app_name = 'core'
router = routers.DefaultRouter()

urlpatterns = [] + url_universidad + url_facultad + url_materia
urlpatterns += router.urls