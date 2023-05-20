from django.urls import path
from.views import sign_up, follow
urlpatterns = [
    path('sign_up/', sign_up),
    path('<int:id>/follow', follow),
    ]
