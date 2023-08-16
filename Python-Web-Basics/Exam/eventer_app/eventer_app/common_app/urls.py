from django.urls import path

from eventer_app.common_app.views import index

urlpatterns = (
    path('', index, name='home-page'),
)