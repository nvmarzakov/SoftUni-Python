from django.urls import path

from eventer_app.events_app.views import dashboard, create_event, details_event, edit_event, delete_event

urlpatterns = (
    path('dashboard/', dashboard, name='dashboard-page'),
    path('create/', create_event, name='create-event-page'),
    path('details/<int:pk>/', details_event, name='details-event-page'),
    path('edit/<int:pk>/', edit_event, name='edit-event-page'),
    path('delete/<int:pk>/', delete_event, name='delete-event-page'),
)