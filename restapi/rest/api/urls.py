from django.urls import path
from rest.views import taskManagerView


urlpatterns = [
    path('task-manager-api/', taskManagerView.as_view() , name='task-manager-view' )
]