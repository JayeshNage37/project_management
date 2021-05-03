from .viewsets import ProjectViewSet
from rest_framework import routers
# from rest_framework_nested import routers

project_router = routers.DefaultRouter()
project_router.register('projects',ProjectViewSet)
## generates:
# /clients/
# /clients/{pk}/