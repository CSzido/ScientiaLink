from django.urls import path
from.views import home, create_research, research, report, report_confirm, profile, field, search
urlpatterns = [
    path('', home),
    path('researches/add', create_research),
    path('research/<int:id>', research),
    path('research/<int:id>/report', report),
    path('research/<int:id>/report/confirm', report_confirm),
    path('profile', profile),
    path('fields/<int:id>', field),
    path('search', search),
    ]
