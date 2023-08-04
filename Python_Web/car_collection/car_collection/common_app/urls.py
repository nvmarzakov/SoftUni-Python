# common_app>urls.py
from django.urls import path

from car_collection.common_app.views import index, catalogue

urlpatterns = (
    path('', index, name='index_page'),
    path('catalogue/', catalogue, name='catalogue_page')
)