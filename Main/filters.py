import django_filters
from.models import Research
from django.contrib.auth.models import User


class ResearchFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Research
        fields = ['title']


class ProfileFilter(django_filters.FilterSet):
    profile__full_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['profile__full_name']