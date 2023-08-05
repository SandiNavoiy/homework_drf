
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include('Course.urls', namespace='course')),
    path('lesson/', include('Lesson.urls', namespace='Lesson')),
    path('user/', include('users.urls', namespace='user')),
    path('pay/', include('pay.urls', namespace='pay')),
]
