from django.urls import path

from pay.apps import PayConfig

app_name = PayConfig.name

from pay.views import (
    PayCreateAPIView,
    PayDestroyAPIView,
    PayListAPIView,
    PayRetrieveAPIView,
    PayUpdateAPIView,
)

urlpatterns = [
    path("create/", PayCreateAPIView.as_view(), name="pay_create"),
    path("list/", PayListAPIView.as_view(), name="pay_list"),
    path("deteil/<int:pk>/", PayRetrieveAPIView.as_view(), name="pay_deteil"),
    path("update/<int:pk>/", PayUpdateAPIView.as_view(), name="pay_update"),
    path("delete/<int:pk>/", PayDestroyAPIView.as_view(), name="pay_delete"),
]
