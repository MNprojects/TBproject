from .models import Photo
import django_filters

class PhotoFilter(django_filters.FilterSet):
    caption = django_filters.CharFilter(lookup_expr='icontains')
    dateTaken_gt = django_filters.DateFilter(name='dateTaken', lookup_expr='date__gte')
    dateTaken_lt = django_filters.DateFilter(name='dateTaken', lookup_expr='date__lte')
    class Meta:
        model = Photo
        fields = ['dateTaken']