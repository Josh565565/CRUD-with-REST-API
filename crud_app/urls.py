from django.urls import path
from .views import PersonListCreateView, PersonRetrieveUpdateDestroyView, PersonByNameRetrieveUpdateDestroyView

urlpatterns = [
    path('api/', PersonListCreateView.as_view(), name='person-list-create'),
    path('api/<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(), name='person-retrieve-update-destroy'),
    path('api/name/<str:name>/', PersonByNameRetrieveUpdateDestroyView.as_view(), name='person-by-name-retrieve-update-destroy'),
]
