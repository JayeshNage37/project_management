from rest_framework import viewsets
from .models import *
from . import serializers

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer

    # if method == 'POST':
    #     return render(request, 'homepage.html')
