from django.urls import path
from .views import general_secretary

urlpatterns = [
    path('home/',general_secretary, name="home_page_urls"),
]
