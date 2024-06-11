from django.urls import path, include
from catalog.views import IndexView

app_name = "catalog"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
