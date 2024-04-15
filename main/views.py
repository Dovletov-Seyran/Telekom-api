from rest_framework import viewsets
from .serializers import ApplicationSerializer, NewsSerializer
from .models import Application, News

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    pagination_by = 5

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_by = 5