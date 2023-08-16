from django.urls import path

from eventer_app.profile_app.views import create_profile, details_profile, edit_profile, delete_profile

urlpatterns = (
    path('create/', create_profile, name='create-profile-page'),
    path('details/', details_profile, name='profile-details-page'),
    path('edit/', edit_profile, name='edit-profile-page'),
    path('delete/', delete_profile, name='delete-profile-page'),
)