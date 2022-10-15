from django.urls import path
from .views import BlogListView

app_name = "users"

urlpatterns = [
    path('', BlogListView.as_view(), name="home")
]

