from django.urls import path, include
from rest_framework import routers
from core.views import TaskViewSet

router = routers.DefaultRouter()
router.register('task', TaskViewSet, basename='task')

urlpatterns = router.urls
