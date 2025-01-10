from django.urls import path
from .views import ActivityListCreateView 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('activities/', ActivityListCreateView.as_view(), name='activity-list-create'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

