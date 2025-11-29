from django_filters import FilterSet
from .models import Course

class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'created_by': ['exact'],
            'price': ['gt', 'lt'],
            'subcategory': ['exact']
        }