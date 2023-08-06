from rest_framework.routers import DefaultRouter

from Course.apps import CourseConfig
from Course.views import CourseViewSet

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [

              ] + router.urls