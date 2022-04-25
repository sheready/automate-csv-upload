from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response

from load_csv.serializers import MovieSerializer

from .models import Movies
# Create your views here.

class MovieViewSet(viewsets.ViewSet):
    def list(self, resquest):
        queryset = Movies.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Movies.objects.all()
        movie = get_object_or_404(queryset, id=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)