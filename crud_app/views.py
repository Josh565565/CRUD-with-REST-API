from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer
from rest_framework.exceptions import NotFound, ValidationError

class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        if 'name' not in serializer.validated_data:
            raise ValidationError("Name is required.")
        serializer.save()

class PersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_object(self):
        try:
            return Person.objects.get(pk=self.kwargs['pk'])
        except Person.DoesNotExist:
            raise NotFound("Person not found")
